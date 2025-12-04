"""
Generic dataset loading utilities for FPS.
"""

from __future__ import annotations

import io
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import pandas as pd
import requests

from src.config.datasets import DATASETS, DEFAULT_DATASET_KEY, DatasetConfig, DatasetFormat


class DatasetLoaderError(RuntimeError):
    """Raised when dataset loading fails."""


def _is_url(path_or_url: str) -> bool:
    parsed = urlparse(path_or_url)
    return parsed.scheme in {"http", "https"}


def _read_from_local(source: str, file_format: DatasetFormat, **read_kwargs: Any) -> pd.DataFrame:
    path = Path(source)
    if not path.exists():
        raise DatasetLoaderError(f"Specified file not found: {path}")

    return _load_with_pandas(path, file_format, **read_kwargs)


def _read_from_url(source: str, file_format: DatasetFormat, **read_kwargs: Any) -> pd.DataFrame:
    response = requests.get(source, timeout=30)
    response.raise_for_status()

    if file_format == "csv":
        buffer = io.StringIO(response.text)
    else:
        buffer = io.BytesIO(response.content)

    return _load_with_pandas(buffer, file_format, **read_kwargs)


def _load_with_pandas(handle: Any, file_format: DatasetFormat, **read_kwargs: Any) -> pd.DataFrame:
    loaders = {
        "csv": pd.read_csv,
        "parquet": pd.read_parquet,
        "json": pd.read_json,
    }

    try:
        df = loaders[file_format](handle, **read_kwargs)
    except KeyError as exc:
        raise DatasetLoaderError(f"Unsupported format: {file_format}") from exc

    if df.empty:
        raise DatasetLoaderError("Loaded dataset is empty.")

    return df


def _load_from_source(source: str, file_format: DatasetFormat, **read_kwargs: Any) -> pd.DataFrame:
    if _is_url(source):
        return _read_from_url(source, file_format, **read_kwargs)
    return _read_from_local(source, file_format, **read_kwargs)


def _resolve_config(dataset_key: str) -> DatasetConfig:
    try:
        return DATASETS[dataset_key]
    except KeyError as exc:
        raise DatasetLoaderError(
            f"Dataset '{dataset_key}' is not declared. Update `src/config/datasets.py`."
        ) from exc


def load_raw_dataset(
    dataset_key: str | None = None,
    *,
    source: str | None = None,
    file_format: DatasetFormat | None = None,
    **read_kwargs: Any,
) -> pd.DataFrame:
    """
    Load a raw dataset either from the registry or from an ad-hoc source.
    """
    using_registry = dataset_key is not None
    using_direct_source = source is not None or file_format is not None

    if using_registry and using_direct_source:
        raise DatasetLoaderError(
            "Choose either `dataset_key` or (`source` + `file_format`), not both."
        )

    if not using_registry and not using_direct_source:
        dataset_key = DEFAULT_DATASET_KEY

    if dataset_key is not None:
        config = _resolve_config(dataset_key)
        return _load_from_source(config.source, config.file_format, **read_kwargs)

    if source is None or file_format is None:
        raise DatasetLoaderError(
            "When `dataset_key` is omitted you must provide both `source` and `file_format`."
        )

    return _load_from_source(source, file_format, **read_kwargs)


