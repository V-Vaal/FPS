"""
Feature type inference utilities for tabular ML.
"""

from __future__ import annotations

from typing import Iterable

import pandas as pd


def infer_feature_types(
    df: pd.DataFrame,
    exclude: Iterable[str] | None = None,
) -> tuple[list[str], list[str]]:
    """
    Infer numerical and categorical feature columns from df.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to analyze.
    exclude : Iterable[str] | None, optional
        Column names to exclude from inference. Defaults to None.

    Returns
    -------
    tuple[list[str], list[str]]
        A tuple containing (numerical_cols, categorical_cols) as lists of column names.

    Notes
    -----
    - Numerical columns: standard integer or float dtypes (int, int64, float, float64, etc.).
    - Categorical columns: object or category dtype columns.
    - Excluded columns are not included in either list.
    """
    exclude_set = set(exclude) if exclude is not None else set()
    
    # Filter out excluded columns
    candidate_cols = [col for col in df.columns if col not in exclude_set]
    
    numerical_cols: list[str] = []
    categorical_cols: list[str] = []
    
    for col in candidate_cols:
        dtype = df[col].dtype
        
        # Check if numerical (int or float types)
        if pd.api.types.is_numeric_dtype(dtype):
            numerical_cols.append(col)
        # Check if categorical (object or category types)
        elif pd.api.types.is_object_dtype(dtype) or pd.api.types.is_categorical_dtype(dtype):
            categorical_cols.append(col)
        # Other dtypes (datetime, etc.) are ignored by default
    
    return numerical_cols, categorical_cols

