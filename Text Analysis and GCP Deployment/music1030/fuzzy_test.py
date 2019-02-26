import os

import pandas as pd
import pytest

from .fuzzy import jaccard_similarity, fuzzy_merge


def test_jaccard():
    assert jaccard_similarity('a', 'b') == 0
    assert jaccard_similarity('c', 'c') == 1
    assert jaccard_similarity('C', 'c') == 1
    assert jaccard_similarity('ace', 'acd') == 2 / 4


def test_fuzzy_merge():
    df1 = pd.DataFrame(['sipping on fire'], columns=['song'])
    df2 = pd.DataFrame(['sippin’ on fire'], columns=['song'])

    actual = fuzzy_merge(df1, df2, on=['song'])

    expected = pd.DataFrame([('sipping on fire', 'sippin’ on fire')],
                            columns=['song_x', 'song_y'])

    assert expected.equals(actual)


def test_fuzzy_merge_string_index():
    df1 = pd.DataFrame(['sipping on fire'], columns=['song'], index=['a'])
    df2 = pd.DataFrame(['sippin’ on fire'], columns=['song'], index=['b'])

    actual = fuzzy_merge(df1, df2, on=['song'])

    expected = pd.DataFrame([('sipping on fire', 'sippin’ on fire')],
                            columns=['song_x', 'song_y'])

    assert expected.equals(actual)


def test_fuzzy_merge_spotify_lastfm_first100(datadir):
    spotify_df = pd.read_csv(os.path.join(datadir, 'spotify.csv'))
    spotify_df = spotify_df[1300:]
    lastfm_df = pd.read_csv(os.path.join(datadir, 'lastfm.csv'))
    actual = fuzzy_merge(spotify_df, lastfm_df,
                         on=['song_name', 'main_artist_name'])
    mask = ((actual['song_name_x'] == 'trees get wheeled away') &
            (actual['song_name_y'] == 'the trees get wheeled away'))
    assert len(actual[mask]) == 1
