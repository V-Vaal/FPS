"""Data loading utilities for the FPS project."""

from pathlib import Path
from typing import Union

import pandas as pd


def load_csv(path: Union[str, Path], **kwargs) -> pd.DataFrame:
    """Load a CSV file and return a pandas DataFrame."""
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    default_kwargs = {"low_memory": False}
    default_kwargs.update(kwargs)
    return pd.read_csv(csv_path, **default_kwargs)
