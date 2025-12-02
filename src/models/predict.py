"""Inference helpers for trained FPS models."""

from pathlib import Path
from typing import Any

import joblib
import pandas as pd


def load_model(path: str | Path) -> Any:
    """Load a serialized model from disk."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Model file not found: {path}")
    return joblib.load(path)


def predict_proba(model: Any, X: pd.DataFrame) -> pd.DataFrame:
    """Return class probabilities as a DataFrame with proper column names."""
    proba = model.predict_proba(X)
    classes = getattr(model, "classes_", range(proba.shape[1]))
    return pd.DataFrame(proba, columns=classes, index=X.index)


def predict_labels(model: Any, X: pd.DataFrame) -> pd.Series:
    """Return predicted labels as a pandas Series."""
    import pandas as pd  # local import to keep top imports minimal

    preds = model.predict(X)
    return pd.Series(preds, index=X.index, name="prediction")


