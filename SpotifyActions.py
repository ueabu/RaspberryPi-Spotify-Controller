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
    card_id_string = str(card_id)

    try:
        mapping = id_to_action_mapping[card_id_string]
    except KeyError:
        print('This card has not been linked to an album')
        return
    
    print("playing "+mapping['name'])
    spotify_body = mapping['spotify_body']
    
    play_endpoint = "{}/me/player/play".format(SPOTIFY_API_URL)

    play_request = requests.put(play_endpoint, headers=authorization_header, data=json.dumps(spotify_body))

    print(play_request.status_code)
    if(play_request.status_code != 204):
        play_request.json()

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