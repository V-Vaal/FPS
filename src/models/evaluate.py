from typing import Dict


def evaluate_model(model, X_test, y_test) -> Dict[str, float]:
    """
    Evaluate a trained model using classification metrics (accuracy, F1, recall). Placeholder only.
    """
    raise NotImplementedError("Placeholder implementation. See ML/AIDD rules before implementing.")

"""Evaluation helpers."""

from typing import Dict

import pandas as pd
from sklearn.metrics import classification_report, f1_score, roc_auc_score


def compute_metrics(y_true: pd.Series, y_pred: pd.Series, y_proba: pd.DataFrame) -> Dict[str, float]:
    """Compute core evaluation metrics for multiclass classification."""
    metrics = {
        "macro_f1": f1_score(y_true, y_pred, average="macro"),
        "roc_auc_ovr": roc_auc_score(y_true, y_proba, multi_class="ovr"),
    }
    return metrics


def summarize_report(y_true: pd.Series, y_pred: pd.Series) -> str:
    """Return a classification report as text."""
    return classification_report(y_true, y_pred)
