import json

import requests

# TODO: You should put your cloud function URL here.
# The URL below links to the TA version
BILLBOARD_URL = 'https://us-central1-personal-198408.cloudfunctions.net' \
                '/handle_billboard'
SPOTIFY_URL = 'https://us-central1-personal-198408.cloudfunctions.net' \
              '/handle_spotify'


def test_handle_billboard():
    response = requests.post(
        BILLBOARD_URL,
        headers={
            'Content-type': 'application/json'
        },
        data=json.dumps([{
            "artist_names": "Justin Bieber",
            "rank": 1,
            "song_name": "What Do You Mean?",
            "week": "2015-09-19"
        }])
    )
    assert response.json() == [
        {"rank": 1,
         "song_name": "What Do You Mean?",
         "week": "2015-09-19",
         "main_artist_name": "justin bieber"
         }
    ]


def test_handle_spotify(datadir):
    data = [{
        "album": {
            "album_type": "album",
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/"
                                   "1E2AEtxaFaJtH0lO7kgNKw"
                    },
                    "href": "https://api.spotify.com/v1/artists/"
                            "1E2AEtxaFaJtH0lO7kgNKw",
                    "id": "1E2AEtxaFaJtH0lO7kgNKw",
                    "name": "Russell Dickerson",
                    "type": "artist",
                    "uri": "spotify:artist:1E2AEtxaFaJtH0lO7kgNKw"
                }
            ],
            "available_markets": [
                "AD",
                "AR",
                "AT",
                "AU",
                "BE",
                "BG",
                "BO",
                "BR",
                "CA",
                "CH",
                "CL",
                "CO",
                "CR",
                "CY",
                "CZ",
                "DE",
                "DK",
                "DO",
                "EC",
                "EE",
                "ES",
                "FI",
                "FR",
                "GB",
                "GR",
                "GT",
                "HK",
                "HN",
                "HU",
                "ID",
                "IE",
                "IS",
                "IT",
                "JP",
                "LI",
                "LT",
                "LU",
                "LV",
                "MC",
                "MT",
                "MX",
                "MY",
                "NI",
                "NL",
                "NO",
                "NZ",
                "PA",
                "PE",
                "PH",
                "PL",
                "PT",
                "PY",
                "SE",
                "SG",
                "SK",
                "SV",
                "TH",
                "TR",
                "TW",
                "US",
                "UY"
            ],
            "external_urls": {
                "spotify": "https://open.spotify.com/album/"
                           "1B6iXA14exgSuBrdHoNqrB"
            },
            "href": "https://api.spotify.com/v1/albums/"
                    "1B6iXA14exgSuBrdHoNqrB",
            "id": "1B6iXA14exgSuBrdHoNqrB",
            "images": [
                {
                    "height": 640,
                    "url": "https://i.scdn.co/image/"
                           "736107f18625aec57f16a6d84ef51820b139a39d",
                    "width": 640
                },
                {
                    "height": 300,
                    "url": "https://i.scdn.co/image/"
                           "3c0f3d5fef38df51cc160f342275171bfe888822",
                    "width": 300
                },
                {
                    "height": 64,
                    "url": "https://i.scdn.co/image/"
                           "d65a7cbb93752e9442c3cb41c80493925bd70eb9",
                    "width": 64
                }
            ],
            "name": "Yours - EP",
            "type": "album",
            "uri": "spotify:album:1B6iXA14exgSuBrdHoNqrB"
        },
        "artists": [
            {
                "external_urls": {
                    "spotify": "https://open.spotify.com/artist/"
                               "1E2AEtxaFaJtH0lO7kgNKw"
                },
                "href": "https://api.spotify.com/v1/artists/"
                        "1E2AEtxaFaJtH0lO7kgNKw",
                "id": "1E2AEtxaFaJtH0lO7kgNKw",
                "name": "Russell Dickerson",
                "type": "artist",
                "uri": "spotify:artist:1E2AEtxaFaJtH0lO7kgNKw"
            }
        ],
        "available_markets": [
            "AD",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "EC",
            "EE",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IS",
            "IT",
            "JP",
            "LI",
            "LT",
            "LU",
            "LV",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "PA",
            "PE",
            "PH",
            "PL",
            "PT",
            "PY",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TR",
            "TW",
            "US",
            "UY"
        ],
        "disc_number": 1,
        "duration_ms": 211240,
        "explicit": False,
        "external_ids": {
            "isrc": "USQX91602319"
        },
        "external_urls": {
            "spotify": "https://open.spotify.com/track/"
                       "6Axy0fL3FBtwx2rwl4soq9"
        },
        "href": "https://api.spotify.com/v1/tracks/6Axy0fL3FBtwx2rwl4soq9",
        "id": "6Axy0fL3FBtwx2rwl4soq9",
        "name": "Blue Tacoma",
        "popularity": 78,
        "preview_url": "https://p.scdn.co/mp3-preview/"
                       "4fd8dd4532f5c256745783bba52750e59af1238f?"
                       "cid=fd8abe6759d345499f8677c6c0adad96",
        "track_number": 4,
        "type": "track",
        "uri": "spotify:track:6Axy0fL3FBtwx2rwl4soq9"
    }]

    response = requests.post(
        SPOTIFY_URL,
        headers={
            'Content-type': 'application/json'
        },
        data=json.dumps(data)
    )

    assert response.json() == [{
        "main_artist_id": "1E2AEtxaFaJtH0lO7kgNKw",
        "main_artist_name": "russell dickerson",
        "popularity": 78,
        "song_id": "6Axy0fL3FBtwx2rwl4soq9",
        "song_length": 211240,
        "song_name": "blue tacoma"
    }]
