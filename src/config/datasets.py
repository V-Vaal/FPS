"""
Centralized dataset registry for the Fraud Prediction System (FPS).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


DatasetFormat = Literal["csv", "parquet", "json"]


@dataclass(frozen=True)
class DatasetConfig:
    key: str
    source: str
    file_format: DatasetFormat
    description: str = ""


DATASETS: dict[str, DatasetConfig] = {
    "demo_fraud": DatasetConfig(
        key="demo_fraud",
        source="data/raw/demo_fraud.csv",
        file_format="csv",
        description="Placeholder dataset. You should replace this entry with your own dataset path or URL.",
    ),
}


DEFAULT_DATASET_KEY = "demo_fraud"


