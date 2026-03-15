"""
End-to-end pipeline: train all models, run inference on new readings,
and produce personalized coaching advice.

Usage (training):
    python -m biosensor.pipeline --mode train --output models/

Usage (inference demo):
    python -m biosensor.pipeline --mode demo
"""

from __future__ import annotations

import argparse
import json
import os
import pickle
from pathlib import Path
from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd

from biosensor.coaching_engine import CoachingEngine
from biosensor.data_models import (
    FEATURE_COLS,
    CyclePhase,
    generate_synthetic_dataset,
)
from biosensor.models import (
    CyclePhaseClassifier,
    MetabolicStateClassifier,
    StressPredictor,
    cross_validate_models,
)


# ---------------------------------------------------------------------------
# BioSensorPipeline — the single entry-point object
# ---------------------------------------------------------------------------

class BioSensorPipeline:
    """
    Orchestrates data → feature engineering → ML models → coaching.

    Attributes
    ----------
    cycle_clf     : CyclePhaseClassifier
    stress_clf    : StressPredictor
    metabolic_clf : MetabolicStateClassifier
    coach         : CoachingEngine
    """

    def __init__(self):
        self.cycle_clf     = CyclePhaseClassifier()
        self.stress_clf    = StressPredictor()
        self.metabolic_clf = MetabolicStateClassifier()
        self.coach         = CoachingEngine()
        self._trained      = False

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def train(self, df: pd.DataFrame, verbose: bool = True) -> Dict[str, float]:
        """
        Train all three models on the provided DataFrame.
        Returns cross-validation accuracy per model.
        """
        if verbose:
            print(f"[Train] Dataset: {len(df)} rows × {len(df.columns)} cols")

        # Cross-validation first
        cv_scores = cross_validate_models(df)
        if verbose:
            print("[CV Scores]")
            for k, v in cv_scores.items():
                print(f"  {k:<25} {v:.3f}")

        # Fit on full dataset
        self.cycle_clf.fit(df, df["cycle_phase"])
        if verbose:
            print("[Cycle Phase Classifier] — fitted")

        self.stress_clf.fit(df, df["stress_level"],
                            cycle_phases=df["cycle_phase"])
        if verbose:
            print("[Stress Predictor]       — fitted")

        self.metabolic_clf.fit(df, df["metabolic_state"])
        if verbose:
            print("[Metabolic Classifier]   — fitted")

        self._trained = True

        if verbose:
            print("\n[Evaluation on training data]")
            print("--- Cycle Phase ---")
            print(self.cycle_clf.evaluate(df, df["cycle_phase"]))
            print("--- Stress Level ---")
            print(self.stress_clf.evaluate(df, df["stress_level"], df["cycle_phase"]))
            print("--- Metabolic State ---")
            print(self.metabolic_clf.evaluate(df, df["metabolic_state"]))

        return cv_scores

    # ------------------------------------------------------------------
    # Inference
    # ------------------------------------------------------------------

    def predict(self, readings: pd.DataFrame) -> pd.DataFrame:
        """
        Run inference on a DataFrame of sensor readings (after feature engineering).
        Returns the DataFrame augmented with prediction columns.
        """
        if not self._trained:
            raise RuntimeError("Call .train() before .predict()")

        out = readings.copy()
        out["pred_cycle_phase"]   = self.cycle_clf.predict(readings)
        out["pred_stress_level"]  = self.stress_clf.predict(
            readings, cycle_phases=out["pred_cycle_phase"]
        )
        out["pred_metabolic"]     = self.metabolic_clf.predict(readings)

        zone_proba_df = self.metabolic_clf.zone_probabilities(readings)
        for col in zone_proba_df.columns:
            out[f"zone_prob_{col}"] = zone_proba_df[col].values

        return out

    # ------------------------------------------------------------------
    # Single reading → coaching advice
    # ------------------------------------------------------------------

    def advise(self, reading: pd.Series) -> "CoachingAdvice":  # noqa: F821
        """
        Takes a single SensorReading as a pd.Series (after feature engineering)
        and returns a CoachingAdvice object.
        """
        row_df = pd.DataFrame([reading])

        cycle_phase    = self.cycle_clf.predict(row_df)[0]
        stress_level   = int(self.stress_clf.predict(row_df, cycle_phases=pd.Series([cycle_phase]))[0])
        stress_proba   = self.stress_clf.predict_proba(row_df, cycle_phases=pd.Series([cycle_phase]))[0].tolist()
        metabolic      = self.metabolic_clf.predict(row_df)[0]
        zone_proba_df  = self.metabolic_clf.zone_probabilities(row_df)
        zone_proba     = {col: float(zone_proba_df[col].iloc[0]) for col in zone_proba_df.columns}

        return self.coach.advise(
            reading           = reading,
            stress_level      = stress_level,
            stress_proba      = stress_proba,
            metabolic_state   = metabolic,
            zone_probabilities= zone_proba,
            cycle_phase       = cycle_phase,
        )

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, path: str | Path) -> None:
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        with open(path / "pipeline.pkl", "wb") as f:
            pickle.dump(self, f)
        print(f"[Save] Pipeline saved to {path / 'pipeline.pkl'}")

    @classmethod
    def load(cls, path: str | Path) -> "BioSensorPipeline":
        with open(Path(path) / "pipeline.pkl", "rb") as f:
            obj = pickle.load(f)
        print(f"[Load] Pipeline loaded from {path}")
        return obj


# ---------------------------------------------------------------------------
# Training script entry-point
# ---------------------------------------------------------------------------

def _train_mode(output_dir: str) -> None:
    print("=" * 60)
    print("   BioSensor ML Pipeline — Training")
    print("=" * 60)

    print("\n[Data] Generating synthetic dataset …")
    df = generate_synthetic_dataset(n_athletes=80, readings_per_athlete=200)
    print(f"       {len(df)} readings generated")

    pipeline = BioSensorPipeline()
    cv_scores = pipeline.train(df, verbose=True)

    pipeline.save(output_dir)

    print("\n[CV Summary]")
    for k, v in cv_scores.items():
        bar = "█" * int(v * 30)
        print(f"  {k:<25} {v:.3f}  {bar}")


def _demo_mode() -> None:
    print("=" * 60)
    print("   BioSensor ML Pipeline — Live Inference Demo")
    print("=" * 60)

    print("\n[Data] Generating synthetic dataset …")
    df = generate_synthetic_dataset(n_athletes=20, readings_per_athlete=100)

    pipeline = BioSensorPipeline()
    pipeline.train(df, verbose=False)
    print("[Model] Training complete.\n")

    # Simulate 5 different real-time readings across different cycle phases
    scenarios = [
        {"label": "Athlète en phase folliculaire — effort modéré",
         "cycle_day": 9,  "cortisol_ug_dl": 7,  "lactate_mmol_l": 2.8,
         "glucose_mg_dl": 112, "il6_pg_ml": 7, "ph": 7.1,
         "sweat_rate_ml": 1.2, "sodium_mmol_l": 55, "potassium_mmol_l": 12,
         "progesterone_pg_ml": 0.5, "estradiol_pg_ml": 180,
         "uric_acid_mg_dl": 3.8},
        {"label": "Athlète en phase lutéale tardive — stress élevé",
         "cycle_day": 26, "cortisol_ug_dl": 19, "lactate_mmol_l": 7.0,
         "glucose_mg_dl": 88, "il6_pg_ml": 35, "ph": 6.85,
         "sweat_rate_ml": 3.5, "sodium_mmol_l": 80, "potassium_mmol_l": 22,
         "progesterone_pg_ml": 3.5, "estradiol_pg_ml": 45,
         "uric_acid_mg_dl": 6.2},
        {"label": "Athlète en phase ovulatoire — pic de performance",
         "cycle_day": 14, "cortisol_ug_dl": 9,  "lactate_mmol_l": 4.5,
         "glucose_mg_dl": 125, "il6_pg_ml": 12, "ph": 7.0,
         "sweat_rate_ml": 2.0, "sodium_mmol_l": 62, "potassium_mmol_l": 14,
         "progesterone_pg_ml": 1.2, "estradiol_pg_ml": 310,
         "uric_acid_mg_dl": 4.1},
        {"label": "Athlète en récupération post-compétition",
         "cycle_day": 5,  "cortisol_ug_dl": 4,  "lactate_mmol_l": 1.1,
         "glucose_mg_dl": 95, "il6_pg_ml": 4, "ph": 7.25,
         "sweat_rate_ml": 0.4, "sodium_mmol_l": 38, "potassium_mmol_l": 9,
         "progesterone_pg_ml": 0.4, "estradiol_pg_ml": 28,
         "uric_acid_mg_dl": 3.1},
        {"label": "ALERTE — Surmenage (overreaching)",
         "cycle_day": 22, "cortisol_ug_dl": 23, "lactate_mmol_l": 13.0,
         "glucose_mg_dl": 62, "il6_pg_ml": 68, "ph": 6.72,
         "sweat_rate_ml": 4.8, "sodium_mmol_l": 95, "potassium_mmol_l": 28,
         "progesterone_pg_ml": 8.0, "estradiol_pg_ml": 90,
         "uric_acid_mg_dl": 7.1},
    ]

    for scenario in scenarios:
        label = scenario.pop("label")
        print(f"\n{'─'*60}")
        print(f"  SCENARIO: {label}")
        print(f"{'─'*60}")

        # Build a one-row dataframe and run feature engineering
        row_df = pd.DataFrame([scenario])
        # Add derived features manually for demo
        row_df["cortisol_to_glucose"]          = row_df["cortisol_ug_dl"] / (row_df["glucose_mg_dl"] + 1e-6)
        row_df["lactate_to_glucose"]           = row_df["lactate_mmol_l"] / (row_df["glucose_mg_dl"] + 1e-6)
        row_df["na_k_ratio"]                   = row_df["sodium_mmol_l"]  / (row_df["potassium_mmol_l"] + 1e-6)
        row_df["estradiol_progesterone_ratio"] = row_df["estradiol_pg_ml"] / (row_df["progesterone_pg_ml"] + 1e-6)
        row_df["cortisol_rolling_mean"]        = row_df["cortisol_ug_dl"]
        row_df["lactate_rolling_std"]          = 0.0
        row_df["cortisol_delta"]               = 0.0
        row_df["inflammatory_score"] = (
            0.5 * (row_df["cortisol_ug_dl"] - 0.5) / 24.5
            + 0.3 * (row_df["il6_pg_ml"] - 1) / 99
            + 0.2 * (row_df["uric_acid_mg_dl"] - 2) / 6
        )
        row_df["hydration_score"] = (
            0.4 * row_df["sweat_rate_ml"] / 5
            + 0.3 * (row_df["sodium_mmol_l"] - 20) / 80
            + 0.3 * (row_df["potassium_mmol_l"] - 5) / 25
        )

        advice = pipeline.advise(row_df.iloc[0])

        print(f"\n  HEADLINE       : {advice.headline}")
        print(f"  Phase cycle    : {advice.cycle_phase}")
        print(f"  Stress         : {['Low','Moderate','High','Critical'][advice.stress_level]}")
        print(f"  Zone metabol.  : {advice.metabolic_state}")
        print(f"  Readiness      : {advice.readiness_score:.0f}/100")
        print(f"\n  COACHING")
        print(f"  Entraînement   : {advice.training_advice}")
        print(f"  Nutrition      : {advice.nutrition_advice}")
        print(f"  Récupération   : {advice.recovery_advice}")
        print(f"  Insight cycle  : {advice.cycle_insight}")
        if advice.alerts:
            print(f"\n  ⚠ ALERTES:")
            for a in advice.alerts:
                print(f"    • {a}")

        top_zones = sorted(advice.zone_probabilities.items(), key=lambda x: -x[1])[:3]
        print(f"\n  Zones (top 3)  : " +
              "  ".join(f"{z}: {p:.0%}" for z, p in top_zones))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="BioSensor ML Pipeline — train or demo"
    )
    parser.add_argument(
        "--mode", choices=["train", "demo"], default="demo",
        help="'train' to fit and save models, 'demo' for inference demo"
    )
    parser.add_argument(
        "--output", default="models/",
        help="Directory to save trained pipeline (train mode only)"
    )
    args = parser.parse_args()

    if args.mode == "train":
        _train_mode(args.output)
    else:
        _demo_mode()
