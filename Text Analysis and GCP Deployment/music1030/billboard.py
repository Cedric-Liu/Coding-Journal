import re

import pandas as pd


def clean_artist_col(artist_names: pd.Series) -> pd.Series:
    # TODO: Task 9
    # YOUR CODE HERE
    pass

def clean_billboard(df: pd.DataFrame) -> pd.DataFrame:
    """Returns a cleaned billboard DataFrame.

    :param df: the billboard DataFrame
    :return a new cleaned DataFrame
    """
    pruned_col = clean_artist_col(df['artist_names'])
    cleaned_df: pd.DataFrame = (df.assign(main_artist_name=pruned_col)
                                .drop_duplicates()
                                .dropna()
                                .drop('artist_names', axis=1))
    return cleaned_df
