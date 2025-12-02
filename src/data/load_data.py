"""
Data loading utilities for the FPS project.

This module provides:
- automated download of the Ethereum fraud dataset using kagglehub
- utilities to load CSV files safely
- a high-level function `load_raw_dataset()` returning a clean DataFrame
"""

from pathlib import Path
from typing import Union

import pandas as pd
import kagglehub


def _download_kaggle_dataset(dataset_name: str) -> Path:
    """
    Download a dataset from Kaggle via kagglehub and return the local path.

    Parameters
    ----------
    dataset_name : str
        The Kaggle dataset identifier, e.g.:
        "fesevu/ethereum-fraud-dataset-by-activity"

    Returns
    -------
    Path
        Path to the local directory containing the dataset.
    """
    local_path = kagglehub.dataset_download(dataset_name)
    return Path(local_path)


def load_csv(path: Union[str, Path], **kwargs) -> pd.DataFrame:
    """
    Load a CSV file and return a pandas DataFrame.

    Parameters
    ----------
    path : str or Path
        Path to the CSV file
    kwargs : dict
        Additional keyword arguments passed to pandas.read_csv

    Returns
    -------
    pd.DataFrame
    """
    csv_path = Path(path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    default_kwargs = {"low_memory": False}
    default_kwargs.update(kwargs)

    return pd.read_csv(csv_path, **default_kwargs)


def load_raw_dataset() -> pd.DataFrame:
    """
    Download and load the raw Ethereum fraud dataset from Kaggle.

    This function:
    - downloads the dataset via kagglehub
    - identifies the correct CSV file(s)
    - loads them into a pandas DataFrame
    - returns the full raw data for further preprocessing

    Returns
    -------
    pd.DataFrame
        The raw Ethereum fraud dataset.
    """
    # Kaggle dataset ID for Ethereum Fraud dataset
    dataset_name = "fesevu/ethereum-fraud-dataset-by-activity"

    # Step 1 — Download dataset locally
    dataset_path = _download_kaggle_dataset(dataset_name)

    # Step 2 — Locate CSV files
    csv_files = list(dataset_path.rglob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in Kaggle dataset path: {dataset_path}"
        )

    # (Optional) If the dataset contains multiple CSVs — pick the main one
    # Here we pick the first, but the notebook will help determine the right file
    raw_csv = csv_files[0]

    # Step 3 — Load into pandas
    df = load_csv(raw_csv)

    return df
