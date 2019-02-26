import flask
import pandas as pd

from music1030.billboard import clean_billboard
from music1030.spotify import clean_spotify_tracks


def handle_billboard(request: flask.Request):
    """

    :param request: a flask Request containing the JSON data
    :return: a
    """
    data = request.get_json()
    df = pd.DataFrame(data)
    cleaned_df: pd.DataFrame = clean_billboard(df)
    cleaned_json = cleaned_df.to_json(orient='records')
    return flask.Response(response=cleaned_json,
                          status=200,
                          mimetype='application/json')


def handle_spotify(request: flask.Request):
    # YOUR CODE HERE
    pass
