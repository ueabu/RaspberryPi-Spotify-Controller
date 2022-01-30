import requests
from Refresh import Refresh
import json

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)


def play():
    authorization_header = getAuthorizationHeader()
    body = {
        "context_uri": "spotify:playlist:6IG6COtztO1Xzvxto0WFN0",
        "offset": {
            "position": 1
        },
        "position_ms": 0
        }

    # Auth Step 6: Use the access token to access Spotify API
    play_endpoint = "{}/me/player/play".format(SPOTIFY_API_URL)

    play_request = requests.put(play_endpoint, headers=authorization_header, data=json.dumps(body))
    # print(play_request.json())
    return 'play_request.status_code'


def pause():
    authorization_header = getAuthorizationHeader()
    pause_profile_endpoint = "{}/me/player/pause".format(SPOTIFY_API_URL)
    pause_request = requests.put(pause_profile_endpoint, headers=authorization_header)
    print((pause_request.status_code))
    return 'pause_request.status_code'


def getAuthorizationHeader():
    refreshCaller = Refresh()
    authorization_header = {"Authorization": "Bearer {}".format(refreshCaller.refresh())}
    return authorization_header