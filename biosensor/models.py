"""
ML models for the sweat biosensor pipeline.

Three specialised estimators:
1. CyclePhaseClassifier  – predicts the menstrual cycle phase from hormone
   and biomarker readings (multi-class classification).
2. StressPredictor       – predicts biochemical stress level (0-3) with
   cycle-aware feature augmentation (gradient boosting).
3. MetabolicStateClassifier – predicts the current metabolic zone from
   lactate, glucose, pH and heart rate (random forest).

All estimators follow the scikit-learn API (fit / predict / predict_proba).
"""

from __future__ import annotations

import warnings
from typing import Tuple, List, Dict, Any

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
    VotingClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.utils.validation import check_is_fitted

from biosensor.data_models import FEATURE_COLS, CyclePhase

warnings.filterwarnings("ignore")


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

CYCLE_FEATURES = [
    "estradiol_pg_ml", "progesterone_pg_ml",
    "estradiol_progesterone_ratio", "cortisol_rolling_mean",
    "cortisol_ug_dl", "il6_pg_ml", "cycle_day",
]

STRESS_FEATURES = [
    "cortisol_ug_dl", "cortisol_rolling_mean", "cortisol_delta",
    "cortisol_to_glucose", "il6_pg_ml", "uric_acid_mg_dl",
    "inflammatory_score", "sweat_rate_ml", "hydration_score",
    "lactate_mmol_l", "glucose_mg_dl",
    # cycle context (hormones modulate stress response)
    "estradiol_pg_ml", "progesterone_pg_ml",
    "estradiol_progesterone_ratio",
]

METABOLIC_FEATURES = [
    "lactate_mmol_l", "lactate_to_glucose", "lactate_rolling_std",
    "glucose_mg_dl", "ph", "cortisol_ug_dl", "sweat_rate_ml",
    "sodium_mmol_l", "potassium_mmol_l", "na_k_ratio",
]


def _select(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    """Return only columns that exist in df."""
    return df[[c for c in cols if c in df.columns]]


# ---------------------------------------------------------------------------
# 1. Cycle Phase Classifier
# ---------------------------------------------------------------------------

class CyclePhaseClassifier(BaseEstimator, ClassifierMixin):
    """
    Predicts the menstrual cycle phase from sweat biomarkers.

    Uses a soft-voting ensemble:
      - Gradient Boosting (handles non-linear hormone curves)
      - Calibrated Logistic Regression (well-calibrated probabilities)
    """

    def __init__(self, n_estimators: int = 200, lr: float = 0.05):
        self.n_estimators = n_estimators
        self.lr = lr

    # ------------------------------------------------------------------
    def fit(self, X: pd.DataFrame, y: pd.Series) -> "CyclePhaseClassifier":
        self.label_encoder_ = LabelEncoder()
        y_enc = self.label_encoder_.fit_transform(y)

        feats = _select(X, CYCLE_FEATURES)
        self.feature_names_ = feats.columns.tolist()

        gb = GradientBoostingClassifier(
            n_estimators=self.n_estimators,
            learning_rate=self.lr,
            max_depth=4,
            subsample=0.8,
            random_state=42,
        )
        lr_cal = CalibratedClassifierCV(
            LogisticRegression(max_iter=1000, C=1.0, random_state=42),
            cv=3,
            method="isotonic",
        )
        self.pipeline_ = Pipeline([
            ("scaler", StandardScaler()),
            ("clf", VotingClassifier(
                estimators=[("gb", gb), ("lr", lr_cal)],
                voting="soft",
                weights=[2, 1],
            )),
        ])
        self.pipeline_.fit(feats.values, y_enc)
        self.classes_ = self.label_encoder_.classes_
        return self

    # ------------------------------------------------------------------
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        check_is_fitted(self, "pipeline_")
        feats = _select(X, self.feature_names_)
        encoded = self.pipeline_.predict(feats.values)
        return self.label_encoder_.inverse_transform(encoded)

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        check_is_fitted(self, "pipeline_")
        feats = _select(X, self.feature_names_)
        return self.pipeline_.predict_proba(feats.values)

    def evaluate(self, X: pd.DataFrame, y: pd.Series) -> str:
        preds = self.predict(X)
        return classification_report(y, preds)


# ---------------------------------------------------------------------------
# 2. Stress Predictor
# ---------------------------------------------------------------------------

class StressPredictor(BaseEstimator, ClassifierMixin):
    """
    Predicts biochemical stress level (0=low, 1=moderate, 2=high, 3=critical).

    Key innovation: receives cycle phase as an extra categorical feature so
    the model learns that e.g. the same cortisol value is more concerning
    in the luteal_late phase than in the follicular phase.
    """

    def __init__(self, n_estimators: int = 300, max_depth: int = 5):
        self.n_estimators = n_estimators
        self.max_depth = max_depth

    # ------------------------------------------------------------------
    def fit(self, X: pd.DataFrame, y: pd.Series,
            cycle_phases: pd.Series | None = None) -> "StressPredictor":
        X_aug = self._augment(X, cycle_phases)
        self.feature_names_ = X_aug.columns.tolist()

        self.model_ = Pipeline([
            ("scaler", StandardScaler()),
            ("clf", GradientBoostingClassifier(
                n_estimators=self.n_estimators,
                max_depth=self.max_depth,
                learning_rate=0.05,
                subsample=0.8,
                min_samples_leaf=10,
                random_state=42,
            )),
        ])
        self.model_.fit(X_aug.values, y.values)
        self.classes_ = np.unique(y.values)
        return self

    # ------------------------------------------------------------------
    def predict(self, X: pd.DataFrame,
                cycle_phases: pd.Series | None = None) -> np.ndarray:
        check_is_fitted(self, "model_")
        X_aug = self._augment(X, cycle_phases)
        return self.model_.predict(X_aug[self.feature_names_].values)

    def predict_proba(self, X: pd.DataFrame,
                      cycle_phases: pd.Series | None = None) -> np.ndarray:
        check_is_fitted(self, "model_")
        X_aug = self._augment(X, cycle_phases)
        return self.model_.predict_proba(X_aug[self.feature_names_].values)

    # ------------------------------------------------------------------
    _ALL_PHASES = [p.value for p in CyclePhase]

    def _augment(self, X: pd.DataFrame,
                 cycle_phases: pd.Series | None) -> pd.DataFrame:
        feats = _select(X, STRESS_FEATURES).copy().reset_index(drop=True)
        if cycle_phases is not None:
            phase_dummies = pd.get_dummies(cycle_phases.reset_index(drop=True),
                                           prefix="phase")
            # Ensure all phase columns are always present (handles unseen phases at inference)
            for phase in self._ALL_PHASES:
                col = f"phase_{phase}"
                if col not in phase_dummies.columns:
                    phase_dummies[col] = 0
            phase_dummies = phase_dummies.sort_index(axis=1)
            feats = pd.concat([feats, phase_dummies], axis=1)
        return feats

    def feature_importances(self) -> pd.Series:
        check_is_fitted(self, "model_")
        clf = self.model_.named_steps["clf"]
        return pd.Series(clf.feature_importances_,
                         index=self.feature_names_).sort_values(ascending=False)

    def evaluate(self, X: pd.DataFrame, y: pd.Series,
                 cycle_phases: pd.Series | None = None) -> str:
        preds = self.predict(X, cycle_phases)
        return classification_report(y, preds,
                                     target_names=["low", "moderate", "high", "critical"])


# ---------------------------------------------------------------------------
# 3. Metabolic State Classifier
# ---------------------------------------------------------------------------

class MetabolicStateClassifier(BaseEstimator, ClassifierMixin):
    """
    Classifies the current metabolic zone based on biochemical markers.

    Uses a Random Forest with probability calibration so that the coaching
    engine can use soft zone probabilities (e.g. "65 % aerobic / 35 % threshold").
    """

    def __init__(self, n_estimators: int = 250, max_depth: int = 8):
        self.n_estimators = n_estimators
        self.max_depth = max_depth

    # ------------------------------------------------------------------
    def fit(self, X: pd.DataFrame, y: pd.Series) -> "MetabolicStateClassifier":
        self.label_encoder_ = LabelEncoder()
        y_enc = self.label_encoder_.fit_transform(y)

        feats = _select(X, METABOLIC_FEATURES)
        self.feature_names_ = feats.columns.tolist()

        rf = RandomForestClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            min_samples_leaf=5,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1,
        )
        self.model_ = Pipeline([
            ("scaler", StandardScaler()),
            ("clf", CalibratedClassifierCV(rf, cv=3, method="isotonic")),
        ])
        self.model_.fit(feats.values, y_enc)
        self.classes_ = self.label_encoder_.classes_
        return self

    # ------------------------------------------------------------------
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        check_is_fitted(self, "model_")
        feats = _select(X, self.feature_names_)
        encoded = self.model_.predict(feats.values)
        return self.label_encoder_.inverse_transform(encoded)

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        check_is_fitted(self, "model_")
        feats = _select(X, self.feature_names_)
        return self.model_.predict_proba(feats.values)

    def zone_probabilities(self, X: pd.DataFrame) -> pd.DataFrame:
        """Returns a DataFrame with one column per metabolic zone."""
        proba = self.predict_proba(X)
        return pd.DataFrame(proba, columns=self.classes_)

    def evaluate(self, X: pd.DataFrame, y: pd.Series) -> str:
        preds = self.predict(X)
        return classification_report(y, preds)


# ---------------------------------------------------------------------------
# Cross-validation utility
# ---------------------------------------------------------------------------

def cross_validate_models(
    df: pd.DataFrame,
) -> Dict[str, float]:
    """
    Run 5-fold stratified CV on all three models and return mean accuracies.
    """
    results: Dict[str, float] = {}
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    # --- Cycle phase ---
    clf = CyclePhaseClassifier()
    feats = _select(df, CYCLE_FEATURES)
    scores = cross_val_score(
        Pipeline([("sc", StandardScaler()), ("clf", GradientBoostingClassifier(random_state=42))]),
        feats.fillna(0), df["cycle_phase"], cv=skf, scoring="accuracy",
    )
    results["cycle_phase_acc"] = float(scores.mean())

    # --- Stress ---
    stress_feats = _select(df, STRESS_FEATURES)
    scores = cross_val_score(
        Pipeline([("sc", StandardScaler()), ("clf", GradientBoostingClassifier(random_state=42))]),
        stress_feats.fillna(0), df["stress_level"], cv=skf, scoring="accuracy",
    )
    results["stress_acc"] = float(scores.mean())

    # --- Metabolic state ---
    met_feats = _select(df, METABOLIC_FEATURES)
    scores = cross_val_score(
        Pipeline([("sc", StandardScaler()), ("clf", RandomForestClassifier(random_state=42, n_jobs=-1))]),
        met_feats.fillna(0), df["metabolic_state"], cv=skf, scoring="accuracy",
    )
    results["metabolic_acc"] = float(scores.mean())

    return results
