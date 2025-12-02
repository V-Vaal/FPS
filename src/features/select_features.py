"""Feature selection helpers."""

from typing import List

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif


def filter_constant_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remove columns with zero variance."""
    return df.loc[:, df.nunique(dropna=False) > 1]


def univariate_selection(X: pd.DataFrame, y: pd.Series, k: int = 20) -> List[str]:
    """Return the top-k feature names using ANOVA F-score."""
    selector = SelectKBest(score_func=f_classif, k=min(k, X.shape[1]))
    selector.fit(X, y)
    return X.columns[selector.get_support()].tolist()
