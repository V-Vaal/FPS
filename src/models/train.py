"""Training utilities for FPS models."""

from dataclasses import dataclass
from typing import Dict, Tuple

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


@dataclass
class TrainingArtifacts:
    model: object
    metrics: Dict[str, float]


def build_models(random_state: int = 42) -> Dict[str, object]:
    """Return the baseline model zoo."""
    return {
        "logreg": LogisticRegression(max_iter=1000, n_jobs=-1),
        "rf": RandomForestClassifier(n_estimators=500, random_state=random_state),
        "xgb": XGBClassifier(
            objective="multi:softprob",
            eval_metric="mlogloss",
            random_state=random_state,
            n_estimators=400,
        ),
    }


def train_model(model, X_train: pd.DataFrame, y_train: pd.Series) -> object:
    """Fit a model and return it."""
    return model.fit(X_train, y_train)
