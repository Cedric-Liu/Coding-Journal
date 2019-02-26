import os

import pandas as pd

from .billboard import clean_artist_col, clean_billboard


def test_prune_dummy():
    dummy1 = pd.Series(data=['Major Lazer & DJ Snake Featuring MO'])
    pruned1 = clean_artist_col(dummy1)
    assert pruned1[0] == 'major lazer'
    dummy2 = pd.Series(data=['Selena Gomez Featuring A$AP Rocky',
                             # The following two lines represent a single row
                             ('Macklemore & Ryan Lewis Featuring Eric Nally,' +
                              'Melle Mel, Kool Moe Dee & Grandmaster Caz'),
                             'Young Thug And Travis Scott Featuring Quavo'])
    pruned2 = clean_artist_col(dummy2)
    assert pruned2[0] == 'selena gomez'
    assert pruned2[1] == 'macklemore'
    assert pruned2[2] == 'young thug'


def test_prune_full(datadir):
    hot100_path = os.path.join(datadir, 'hot100.csv')
    df = pd.read_csv(hot100_path)
    df_copy = df.copy()

    pruned_col = clean_artist_col(df['artist_names'])

    assert not pruned_col.str.contains(' and ').any()
    assert not pruned_col.str.contains('&').any()
    assert not pruned_col.str.contains(' featuring').any()
    assert df.equals(df_copy)


def test_clean_partial(datadir):
    hot100_path = os.path.join(datadir, 'hot100.csv')
    df = pd.read_csv(hot100_path)
    df_copy = df.copy()

    cleaned = clean_billboard(df.iloc[0:10])

    assert 'song_name' in cleaned.columns
    assert 'rank' in cleaned.columns
    assert 'week' in cleaned.columns
    assert not df.isnull().values.any()
    assert not df.duplicated().any()
    assert df.equals(df_copy)


def test_clean_full(datadir):
    hot100_path = os.path.join(datadir, 'hot100.csv')
    df = pd.read_csv(hot100_path)
    df_copy = df.copy()

    cleaned = clean_billboard(df)

    assert 'song_name' in cleaned.columns
    assert 'rank' in cleaned.columns
    assert 'week' in cleaned.columns
    assert not df.isnull().values.any()
    assert not df.duplicated().any()
    assert df.equals(df_copy)
