from collections import Counter
from typing import List

import pandas as pd


def jaccard_similarity(a: str,
                       b: str) -> float:
    """Takes in two strings and computes their letter-wise
    Jaccard similarity for bags.

    Case should be ignored.
    """
    # TODO: Task 3
    # YOUR CODE HERE
    pass


def fuzzy_merge(left: pd.DataFrame,
                right: pd.DataFrame,
                on: List[str]) -> pd.DataFrame:
    """Merge DataFrame objects by performing a fuzzy
    database-style join operation by columns.

    :param left: a DataFrame
    :param right: a DataFrame
    :param on: Column or index level names to join on. These must be
    found in both DataFrames.
    :return: the merged DataFrame
    """
    # TODO: Task 3
    # YOUR CODE HERE
    pass
