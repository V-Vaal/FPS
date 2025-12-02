"""Feature extraction utilities."""

from typing import Dict

import pandas as pd


def add_activity_ratios(df: pd.DataFrame) -> pd.DataFrame:
    """Create ratio-based features from transaction counts."""
    df = df.copy()
    denom = df["tx_count"].replace(0, 1)
    df["success_ratio"] = df.get("success_tx", 0) / denom
    df["failed_ratio"] = df.get("failed_tx", 0) / denom
    return df


def summarize_time_windows(df: pd.DataFrame, windows: Dict[str, int]) -> pd.DataFrame:
    """Placeholder for rolling aggregations on temporal data."""
    _ = windows
    return df
