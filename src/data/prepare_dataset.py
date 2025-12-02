import pandas as pd


def prepare_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess the raw dataframe: rename columns, handle missing values, normalize types. Placeholder only.
    """
    raise NotImplementedError("Placeholder implementation. See ML/AIDD rules before implementing.")

"""Dataset preparation helpers for FPS."""

from typing import Iterable

import pandas as pd


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Strip whitespace and lowercase column names for consistency."""
    df = df.copy()
    df.columns = [col.strip().lower() for col in df.columns]
    return df


def drop_leaky_features(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    """Remove columns that leak target information."""
    return df.drop(columns=list(columns), errors="ignore")
