import requests
from Refresh import Refresh
import json

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

def get_id_json_mapping():
    with open('id_to_playlist_mapping.json', 'r') as mapping_file:
        mapping_file_json = json.load(mapping_file)

    return mapping_file_json


def play(card_id):
    authorization_header = getAuthorizationHeader()

    id_to_action_mapping = get_id_json_mapping()

    body = id_to_action_mapping[card_id]
    print(body)
    

    # if card_id == 1047477723963:
    #     body = {
    #         "context_uri": "spotify:playlist:6IG6COtztO1Xzvxto0WFN0",
    #         "offset": {
    #             "position": 1
    #         },
    #         "position_ms": 0
    #         }
    # elif card_id == 222959766951:
    #     body = {
    #         "context_uri": "spotify:album:4dZjYBEciWomanesAv3fie",
    #         "offset": {
    #             "position": 4
    #         },
    #         "position_ms": 0
    #         }

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

def shuffle():
    authorization_header = getAuthorizationHeader()
    pause_profile_endpoint = "{}/me/player/pause".format(SPOTIFY_API_URL)
    pause_request = requests.put(pause_profile_endpoint, headers=authorization_header)
    print((pause_request.status_code))
    return 'pause_request.status_code'


def getAuthorizationHeader():
    refreshCaller = Refresh()
    authorization_header = {"Authorization": "Bearer {}".format(refreshCaller.refresh())}
    return authorization_header