"""
Data models and feature engineering for the sweat biosensor patch.

Biomarkers measured:
  - Cortisol       (stress hormone, µg/dL)
  - Lactate        (metabolic effort, mmol/L)
  - Glucose        (energy availability, mg/dL)
  - IL-6           (inflammation, pg/mL)
  - Uric acid      (oxidative stress, mg/dL)
  - pH             (metabolic acidosis)
  - Sweat rate     (mL/cm²/min)
  - Na⁺ / K⁺      (electrolyte balance, mmol/L)
  - Progesterone   (cycle estimation, pg/mL — optical sensor)
  - Estradiol      (cycle estimation, pg/mL — optical sensor)
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Domain enums
# ---------------------------------------------------------------------------

class CyclePhase(Enum):
    MENSTRUAL    = "menstrual"       # days 1-5
    FOLLICULAR   = "follicular"      # days 6-13
    OVULATORY    = "ovulatory"       # days 14-16
    LUTEAL_EARLY = "luteal_early"    # days 17-22
    LUTEAL_LATE  = "luteal_late"     # days 23-28 (PMS window)


class StressLevel(Enum):
    LOW      = 0
    MODERATE = 1
    HIGH     = 2
    CRITICAL = 3


class MetabolicState(Enum):
    RECOVERY      = "recovery"
    FAT_BURNING   = "fat_burning"
    AEROBIC       = "aerobic"
    THRESHOLD     = "threshold"
    ANAEROBIC     = "anaerobic"
    OVERREACHING  = "overreaching"


# ---------------------------------------------------------------------------
# Raw sensor reading
# ---------------------------------------------------------------------------

@dataclass
class SensorReading:
    """One time-stamped reading from the biosensor patch."""
    timestamp: pd.Timestamp

    # Stress / inflammation
    cortisol_ug_dl: float        # 0.5 – 25
    il6_pg_ml: float             # 1 – 100
    uric_acid_mg_dl: float       # 2 – 8

    # Metabolic
    lactate_mmol_l: float        # 0.5 – 20
    glucose_mg_dl: float         # 60 – 200
    ph: float                    # 6.5 – 8.0

    # Electrolytes / hydration
    sweat_rate_ml: float         # 0 – 5
    sodium_mmol_l: float         # 20 – 100
    potassium_mmol_l: float      # 5 – 30

    # Cycle hormones (estimated from optical reflectance)
    progesterone_pg_ml: float    # 0.1 – 25
    estradiol_pg_ml: float       # 10 – 400

    # Contextual
    heart_rate_bpm: Optional[float] = None
    skin_temp_celsius: Optional[float] = None
    cycle_day: Optional[int] = None   # 1-28, provided by user if known


# ---------------------------------------------------------------------------
# Feature engineering
# ---------------------------------------------------------------------------

FEATURE_COLS = [
    "cortisol_ug_dl", "il6_pg_ml", "uric_acid_mg_dl",
    "lactate_mmol_l", "glucose_mg_dl", "ph",
    "sweat_rate_ml", "sodium_mmol_l", "potassium_mmol_l",
    "progesterone_pg_ml", "estradiol_pg_ml",
    # derived
    "cortisol_to_glucose", "lactate_to_glucose",
    "na_k_ratio", "cortisol_rolling_mean", "lactate_rolling_std",
    "cortisol_delta", "estradiol_progesterone_ratio",
    "inflammatory_score", "hydration_score",
]


def engineer_features(df: pd.DataFrame, window: int = 5) -> pd.DataFrame:
    """
    Add derived features to a DataFrame of SensorReadings (rows).
    Expects columns matching SensorReading field names.
    """
    df = df.copy()

    # Ratios
    df["cortisol_to_glucose"]          = df["cortisol_ug_dl"] / (df["glucose_mg_dl"] + 1e-6)
    df["lactate_to_glucose"]           = df["lactate_mmol_l"] / (df["glucose_mg_dl"] + 1e-6)
    df["na_k_ratio"]                   = df["sodium_mmol_l"]  / (df["potassium_mmol_l"] + 1e-6)
    df["estradiol_progesterone_ratio"] = df["estradiol_pg_ml"] / (df["progesterone_pg_ml"] + 1e-6)

    # Rolling statistics (temporal context)
    df["cortisol_rolling_mean"] = (
        df["cortisol_ug_dl"].rolling(window, min_periods=1).mean()
    )
    df["lactate_rolling_std"] = (
        df["lactate_mmol_l"].rolling(window, min_periods=1).std().fillna(0)
    )

    # Rate of change
    df["cortisol_delta"] = df["cortisol_ug_dl"].diff().fillna(0)

    # Composite scores
    df["inflammatory_score"] = (
        0.5 * _norm(df["cortisol_ug_dl"], 0.5, 25)
        + 0.3 * _norm(df["il6_pg_ml"], 1, 100)
        + 0.2 * _norm(df["uric_acid_mg_dl"], 2, 8)
    )

    df["hydration_score"] = (
        0.4 * _norm(df["sweat_rate_ml"], 0, 5)
        + 0.3 * _norm(df["sodium_mmol_l"], 20, 100)
        + 0.3 * _norm(df["potassium_mmol_l"], 5, 30)
    )

    return df


def _norm(series: pd.Series, lo: float, hi: float) -> pd.Series:
    return (series - lo) / (hi - lo + 1e-9)


# ---------------------------------------------------------------------------
# Synthetic data generator (for training / demo)
# ---------------------------------------------------------------------------

RNG = np.random.default_rng(42)


def generate_synthetic_dataset(n_athletes: int = 80,
                                readings_per_athlete: int = 200) -> pd.DataFrame:
    """
    Generate a realistic synthetic dataset of sensor readings with labels.
    Labels: stress_level (int 0-3), metabolic_state (str), cycle_phase (str).
    """
    rows = []
    for athlete_id in range(n_athletes):
        # Each athlete has a slightly different baseline (inter-individual variability)
        baseline = {
            "cortisol_offset": RNG.uniform(-2, 2),
            "lactate_offset":  RNG.uniform(-0.5, 0.5),
            "glucose_offset":  RNG.uniform(-10, 10),
        }

        for t in range(readings_per_athlete):
            # Simulate cycle day progression (1-28)
            cycle_day = (t % 28) + 1
            phase = _cycle_phase(cycle_day)

            # Hormonal context
            estradiol    = _estradiol_profile(cycle_day)  + RNG.normal(0, 10)
            progesterone = _progesterone_profile(cycle_day) + RNG.normal(0, 1)

            # Stress and metabolic state depend on phase & random workout intensity
            intensity = RNG.choice([0, 1, 2, 3], p=[0.3, 0.35, 0.25, 0.1])

            cortisol  = _cortisol(intensity, phase) + baseline["cortisol_offset"] + RNG.normal(0, 0.5)
            lactate   = _lactate(intensity) + baseline["lactate_offset"] + RNG.normal(0, 0.3)
            glucose   = _glucose(intensity) + baseline["glucose_offset"] + RNG.normal(0, 5)
            il6       = _il6(intensity) + RNG.normal(0, 2)
            uric_acid = 3.5 + 0.5 * intensity + RNG.normal(0, 0.4)
            ph        = 7.2 - 0.05 * intensity + RNG.normal(0, 0.05)
            sweat     = 0.5 + 0.8 * intensity + RNG.normal(0, 0.15)
            sodium    = 50 + 5 * intensity + RNG.normal(0, 5)
            potassium = 10 + 2 * intensity + RNG.normal(0, 1)

            stress_label    = intensity
            metabolic_label = _metabolic_label(lactate, intensity)

            rows.append({
                "athlete_id":           athlete_id,
                "timestamp":            pd.Timestamp("2025-01-01") + pd.Timedelta(hours=t),
                "cortisol_ug_dl":       np.clip(cortisol, 0.5, 25),
                "il6_pg_ml":            np.clip(il6, 0.1, 100),
                "uric_acid_mg_dl":      np.clip(uric_acid, 1, 10),
                "lactate_mmol_l":       np.clip(lactate, 0.5, 20),
                "glucose_mg_dl":        np.clip(glucose, 40, 250),
                "ph":                   np.clip(ph, 6.3, 8.0),
                "sweat_rate_ml":        np.clip(sweat, 0, 5),
                "sodium_mmol_l":        np.clip(sodium, 10, 120),
                "potassium_mmol_l":     np.clip(potassium, 3, 40),
                "progesterone_pg_ml":   np.clip(progesterone, 0.1, 30),
                "estradiol_pg_ml":      np.clip(estradiol, 5, 500),
                "cycle_day":            cycle_day,
                # Labels
                "stress_level":         stress_label,
                "metabolic_state":      metabolic_label,
                "cycle_phase":          phase.value,
            })

    df = pd.DataFrame(rows)
    return engineer_features(df)


# ---------------------------------------------------------------------------
# Physiological profile helpers
# ---------------------------------------------------------------------------

def _cycle_phase(day: int) -> CyclePhase:
    if day <= 5:   return CyclePhase.MENSTRUAL
    if day <= 13:  return CyclePhase.FOLLICULAR
    if day <= 16:  return CyclePhase.OVULATORY
    if day <= 22:  return CyclePhase.LUTEAL_EARLY
    return CyclePhase.LUTEAL_LATE


def _estradiol_profile(day: int) -> float:
    """Simplified biphasic estradiol curve (pg/mL)."""
    # Peak around ovulation (~day 14), secondary peak luteal (~day 21)
    return (
        250 * np.exp(-0.05 * (day - 14) ** 2)
        + 120 * np.exp(-0.08 * (day - 21) ** 2)
        + 30
    )


def _progesterone_profile(day: int) -> float:
    """Progesterone rises after ovulation, peaks luteal."""
    if day < 14:
        return 0.5
    return 0.5 + 15 * np.exp(-0.05 * (day - 21) ** 2)


def _cortisol(intensity: int, phase: CyclePhase) -> float:
    base = {0: 3, 1: 8, 2: 14, 3: 20}[intensity]
    # Cortisol slightly elevated in luteal phase (PMS)
    if phase in (CyclePhase.LUTEAL_LATE,):
        base *= 1.15
    return base


def _lactate(intensity: int) -> float:
    return {0: 1.0, 1: 2.5, 2: 5.0, 3: 12.0}[intensity]


def _glucose(intensity: int) -> float:
    return {0: 95, 1: 110, 2: 130, 3: 85}[intensity]   # drops at high intensity


def _il6(intensity: int) -> float:
    return {0: 2, 1: 8, 2: 20, 3: 55}[intensity]


def _metabolic_label(lactate: float, intensity: int) -> str:
    if lactate < 1.5:              return MetabolicState.RECOVERY.value
    if lactate < 2.0:              return MetabolicState.FAT_BURNING.value
    if lactate < 4.0:              return MetabolicState.AEROBIC.value
    if lactate < 6.0:              return MetabolicState.THRESHOLD.value
    if intensity < 3:              return MetabolicState.ANAEROBIC.value
    return MetabolicState.OVERREACHING.value
