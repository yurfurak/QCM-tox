"""
Personalized coaching recommendation engine.

Takes real-time biosensor predictions and produces actionable coaching advice
adapted to:
  - Current stress level and its trend
  - Active metabolic zone and zone probabilities
  - Menstrual cycle phase (and associated physiology)
  - Individual athlete profile and history

Output: CoachingAdvice — a structured recommendation object that can be
rendered on a companion app / wearable screen.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import numpy as np
import pandas as pd

from biosensor.data_models import CyclePhase, StressLevel, MetabolicState


# ---------------------------------------------------------------------------
# Coaching advice dataclass
# ---------------------------------------------------------------------------

@dataclass
class CoachingAdvice:
    """Structured coaching recommendation returned by the engine."""
    # Detected states
    cycle_phase: str
    stress_level: int          # 0-3
    metabolic_state: str

    # Primary messages
    headline: str
    training_advice: str
    nutrition_advice: str
    recovery_advice: str

    # Cycle-specific insight
    cycle_insight: str

    # Alerts (non-empty when physiological warning detected)
    alerts: List[str] = field(default_factory=list)

    # Quantitative context (for the app dashboard)
    zone_probabilities: Dict[str, float] = field(default_factory=dict)
    stress_proba: List[float] = field(default_factory=list)   # [low, mod, high, crit]
    readiness_score: float = 0.0   # 0-100

    def to_dict(self) -> dict:
        return self.__dict__.copy()


# ---------------------------------------------------------------------------
# Cycle phase physiology database
# ---------------------------------------------------------------------------

CYCLE_PHYSIOLOGY: Dict[str, Dict] = {
    CyclePhase.MENSTRUAL.value: {
        "hormone_context": "Estradiol & progesterone at nadir. Prostaglandins high.",
        "pain_risk": True,
        "recommended_intensity": "low–moderate",
        "nutrition_tip": "Iron-rich foods (spinach, lentils). Stay hydrated. Reduce inflammatory foods.",
        "recovery_tip": "Prioritise sleep & gentle mobility work. Cold therapy may ease cramps.",
        "training_tip": "Avoid maximal-effort sessions. Yoga, swimming or light cardio are ideal.",
        "insight": "Your hormonal environment is at its lowest. Listen to your body — moderate effort is enough.",
    },
    CyclePhase.FOLLICULAR.value: {
        "hormone_context": "Rising estradiol boosts insulin sensitivity and mood.",
        "pain_risk": False,
        "recommended_intensity": "moderate–high",
        "nutrition_tip": "Higher carbohydrate availability. Add lean protein to support muscle synthesis.",
        "recovery_tip": "Recovery is faster in this phase — ideal for back-to-back training days.",
        "training_tip": "Best phase for strength gains, speed work and new PBs. Push hard.",
        "insight": "Estradiol is rising — your strength, coordination and mood are at their best. Peak training window.",
    },
    CyclePhase.OVULATORY.value: {
        "hormone_context": "Estradiol peak + LH surge. Ligament laxity increases.",
        "pain_risk": False,
        "recommended_intensity": "high (with caution on joints)",
        "nutrition_tip": "Maintain carbohydrate intake. Hydration critical as core temp is slightly elevated.",
        "recovery_tip": "Warm-up & cool-down longer. Pay attention to knee and ankle stability.",
        "training_tip": "High power output available. Be cautious with change-of-direction drills — ligament laxity is heightened.",
        "insight": "Peak physical power — but estradiol increases ACL/MCL laxity. Prioritise joint-safe warm-up.",
    },
    CyclePhase.LUTEAL_EARLY.value: {
        "hormone_context": "Progesterone rises, slightly elevating core temp and ventilation.",
        "pain_risk": False,
        "recommended_intensity": "moderate–high",
        "nutrition_tip": "Increase protein intake to offset progesterone-driven catabolism. Healthy fats support hormone synthesis.",
        "recovery_tip": "Core temp elevated — cool-down carefully. Sleep quality may dip slightly.",
        "training_tip": "Cardio endurance is well-supported. Strength work remains productive.",
        "insight": "Progesterone creates a slightly catabolic environment — prioritise protein at each meal.",
    },
    CyclePhase.LUTEAL_LATE.value: {
        "hormone_context": "Both hormones declining. Cortisol reactivity elevated. PMS risk.",
        "pain_risk": True,
        "recommended_intensity": "low–moderate",
        "nutrition_tip": "Magnesium-rich foods (dark chocolate, nuts) reduce PMS symptoms. Limit caffeine and alcohol.",
        "recovery_tip": "Sleep extension helps blunt cortisol spikes. Meditation and breathwork are powerful here.",
        "training_tip": "De-load or active recovery week. Avoid overtraining — cortisol is already elevated.",
        "insight": "Late luteal phase: cortisol is more reactive. This is NOT the time to push — strategic rest now = better performance next cycle.",
    },
}


# ---------------------------------------------------------------------------
# Metabolic zone advice
# ---------------------------------------------------------------------------

METABOLIC_ADVICE: Dict[str, Dict] = {
    MetabolicState.RECOVERY.value: {
        "training": "You are in recovery zone. Focus on form, mobility, or complete rest.",
        "nutrition": "Light snack with protein (Greek yogurt, boiled egg). No need for high carbs.",
    },
    MetabolicState.FAT_BURNING.value: {
        "training": "Optimal fat-oxidation zone. Maintain steady low-intensity effort for endurance.",
        "nutrition": "Healthy fats and low-GI carbs. Avoid sugar spikes that shift you out of fat burning.",
    },
    MetabolicState.AEROBIC.value: {
        "training": "Aerobic zone — sustainable effort. Good for building aerobic base and stamina.",
        "nutrition": "Balanced meal with 60 % carbs, 20 % protein, 20 % fat 2 h before session.",
    },
    MetabolicState.THRESHOLD.value: {
        "training": "At your lactate threshold. Powerful training zone — keep effort controlled.",
        "nutrition": "Fast carbohydrates during session (banana, energy gel). Protein recovery within 30 min.",
    },
    MetabolicState.ANAEROBIC.value: {
        "training": "Anaerobic zone. High-intensity effort — short duration only.",
        "nutrition": "Carbohydrate loading 3 h before. Immediate post-session: carbs + fast protein (whey).",
    },
    MetabolicState.OVERREACHING.value: {
        "training": "STOP or drastically reduce intensity. Overreaching detected — injury & burnout risk.",
        "nutrition": "Immediate carbohydrate refuel. Anti-inflammatory foods (turmeric, berries). Hydration critical.",
    },
}


# ---------------------------------------------------------------------------
# Alert rules
# ---------------------------------------------------------------------------

def _generate_alerts(reading: pd.Series, stress_level: int) -> List[str]:
    alerts = []

    if reading.get("cortisol_ug_dl", 0) > 20:
        alerts.append("Cortisol critically elevated (>20 µg/dL). Consider aborting today's session.")
    if reading.get("lactate_mmol_l", 0) > 10:
        alerts.append("Lactate >10 mmol/L — severe metabolic acidosis. Stop and recover immediately.")
    if reading.get("glucose_mg_dl", 100) < 65:
        alerts.append("Hypoglycemia risk: blood glucose below 65 mg/dL. Take fast carbohydrates now.")
    if reading.get("ph", 7.0) < 6.8:
        alerts.append("Sweat pH <6.8 — significant metabolic acidosis. Reduce intensity.")
    if reading.get("il6_pg_ml", 0) > 50:
        alerts.append("IL-6 highly elevated — systemic inflammation. Training is counter-productive today.")
    if reading.get("hydration_score", 1) > 0.85:
        alerts.append("Heavy sweating + high electrolyte loss. Hydrate with an electrolyte drink now.")
    if stress_level == 3:
        alerts.append("Critical stress signature. Full rest day recommended.")

    return alerts


# ---------------------------------------------------------------------------
# Readiness score (0–100)
# ---------------------------------------------------------------------------

def _readiness_score(
    stress_level: int,
    metabolic_state: str,
    cycle_phase: str,
    cortisol: float,
    lactate: float,
    glucose: float,
) -> float:
    """Composite readiness score based on biomarkers and cycle context."""
    # Base score from stress (inversely correlated)
    stress_penalty = {0: 0, 1: 15, 2: 35, 3: 55}[stress_level]

    # Metabolic state contribution
    metabolic_bonus = {
        MetabolicState.RECOVERY.value:     5,
        MetabolicState.FAT_BURNING.value: 15,
        MetabolicState.AEROBIC.value:     20,
        MetabolicState.THRESHOLD.value:   10,
        MetabolicState.ANAEROBIC.value:   -5,
        MetabolicState.OVERREACHING.value: -30,
    }.get(metabolic_state, 0)

    # Cycle phase modifier
    phase_mod = {
        CyclePhase.MENSTRUAL.value:    -10,
        CyclePhase.FOLLICULAR.value:   +15,
        CyclePhase.OVULATORY.value:    +12,
        CyclePhase.LUTEAL_EARLY.value:  +5,
        CyclePhase.LUTEAL_LATE.value:  -12,
    }.get(cycle_phase, 0)

    # Biomarker adjustments
    cortisol_pen  = max(0, (cortisol - 10) * 1.5)
    lactate_pen   = max(0, (lactate  - 4)  * 2.0)
    glucose_pen   = max(0, (80 - glucose)  * 0.5) if glucose < 80 else 0

    score = 70 - stress_penalty + metabolic_bonus + phase_mod - cortisol_pen - lactate_pen - glucose_pen
    return float(np.clip(score, 0, 100))


# ---------------------------------------------------------------------------
# Main coaching engine
# ---------------------------------------------------------------------------

class CoachingEngine:
    """
    Combines predictions from the three ML models into personalised advice.

    Usage:
        engine = CoachingEngine()
        advice = engine.advise(reading_series, stress_pred, stress_proba,
                               metabolic_pred, zone_probas, cycle_pred)
    """

    def advise(
        self,
        reading: pd.Series,
        stress_level: int,
        stress_proba: List[float],
        metabolic_state: str,
        zone_probabilities: Dict[str, float],
        cycle_phase: str,
    ) -> CoachingAdvice:

        physio = CYCLE_PHYSIOLOGY.get(cycle_phase, {})
        met    = METABOLIC_ADVICE.get(metabolic_state, {})

        alerts = _generate_alerts(reading, stress_level)

        cortisol = float(reading.get("cortisol_ug_dl", 10))
        lactate  = float(reading.get("lactate_mmol_l", 2))
        glucose  = float(reading.get("glucose_mg_dl", 90))

        readiness = _readiness_score(
            stress_level, metabolic_state, cycle_phase,
            cortisol, lactate, glucose,
        )

        # Headline
        stress_label = ["faible", "modéré", "élevé", "critique"][stress_level]
        headline = (
            f"Indice de forme : {readiness:.0f}/100 — "
            f"Stress biochimique {stress_label} — "
            f"Zone métabolique : {metabolic_state.replace('_', ' ').title()}"
        )

        return CoachingAdvice(
            cycle_phase        = cycle_phase,
            stress_level       = stress_level,
            metabolic_state    = metabolic_state,
            headline           = headline,
            training_advice    = physio.get("training_tip", met.get("training", "Entraînement adapté recommandé.")),
            nutrition_advice   = physio.get("nutrition_tip", met.get("nutrition", "Alimentation équilibrée.")),
            recovery_advice    = physio.get("recovery_tip", "Repos et hydratation."),
            cycle_insight      = physio.get("insight", ""),
            alerts             = alerts,
            zone_probabilities = zone_probabilities,
            stress_proba       = stress_proba,
            readiness_score    = readiness,
        )

    # ------------------------------------------------------------------
    # Batch advisory — useful for weekly trend analysis
    # ------------------------------------------------------------------

    def weekly_trend_report(self, history: pd.DataFrame) -> Dict:
        """
        Summarise a week of readings into a trend report.
        history must have columns: stress_level, metabolic_state,
                                   cycle_phase, readiness_score
        """
        report = {
            "mean_readiness":      float(history["readiness_score"].mean()),
            "stress_distribution": history["stress_level"].value_counts(normalize=True).to_dict(),
            "dominant_metabolic":  history["metabolic_state"].mode().iloc[0],
            "dominant_phase":      history["cycle_phase"].mode().iloc[0],
            "high_stress_days":    int((history["stress_level"] >= 2).sum()),
            "overreaching_events": int((history["metabolic_state"] == MetabolicState.OVERREACHING.value).sum()),
        }

        # Personalised weekly suggestion
        if report["high_stress_days"] >= 4:
            report["weekly_recommendation"] = (
                "Semaine fortement stressée (≥4 jours). "
                "Intégrer 2 jours de récupération active et réduire le volume total de 20 %."
            )
        elif report["mean_readiness"] > 75:
            report["weekly_recommendation"] = (
                "Excellente semaine de forme ! "
                "Vous pouvez programmer une séance de qualité haute intensité dans les 48 h."
            )
        else:
            report["weekly_recommendation"] = (
                "Semaine correcte. Maintenir l'équilibre entraînement/récupération actuel."
            )

        return report
