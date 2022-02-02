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


def decode_card_to_action(card_id):
   
    id_to_action_mapping = get_id_json_mapping()
    card_id_string = str(card_id)

    try:
        mapping = id_to_action_mapping[card_id_string]
    except KeyError:
        print('This card has not been linked to a command')
        return
    
    if mapping['type'] == 'play':
        print("playing "+mapping['name'])
        play(mapping['spotify_body'])
    elif mapping['type'] == 'control':
        if mapping['name'] == 'Shuffle And Play Next':
            print('Shuffling')
            shuffle(id_to_action_mapping['shuffle']['spotify_body'])
            print('Playing Next')
            play_next(id_to_action_mapping['play_next']['spotify_body'])
        elif mapping['name'] == 'Play Next':
            print('Playing Next')
            play_next(id_to_action_mapping['play_next']['spotify_body'])
        elif mapping['name'] == 'Pause':
            print('Pausing')
            play_next(id_to_action_mapping['pause']['spotify_body'])



    # print("playing "+mapping['name'])
    # spotify_body = mapping['spotify_body']
    
    # play_endpoint = "{}/me/player/play".format(SPOTIFY_API_URL)

    # play_request = requests.put(play_endpoint, headers=authorization_header, data=json.dumps(spotify_body))

    # print(play_request.status_code)
    # if(play_request.status_code != 204):
    #     play_request.json()

    # return 'play_request.status_code'


def play(spotify_body):
    authorization_header = getAuthorizationHeader()
    play_endpoint = "{}/me/player/play".format(SPOTIFY_API_URL)

    play_request = requests.put(play_endpoint, headers=authorization_header, data=json.dumps(spotify_body))

    print(play_request.status_code)
    if(play_request.status_code != 204):
        play_request.json()

    return play_request.status_code

def shuffle(spotify_body):
    authorization_header = getAuthorizationHeader()
    shuffle_endpoint = "{}/me/player/shuffle".format(SPOTIFY_API_URL)

    shuffle_request = requests.put(shuffle_endpoint, headers=authorization_header, data=json.dumps(spotify_body))

    print(shuffle_request.status_code)
    if(shuffle_request.status_code != 204):
        shuffle_request.json()
    return shuffle_request.status_code

def play_next(spotify_body):
    authorization_header = getAuthorizationHeader()
    play_next_endpoint = "{}/me/player/next".format(SPOTIFY_API_URL)
    play_next_request = requests.post(play_next_endpoint, headers=authorization_header, data=json.dumps(spotify_body))
    print(play_next_request.status_code)
    if(play_next_request.status_code != 204):
        play_next_request.json()
    return play_next_request.status_code


def pause():
    authorization_header = getAuthorizationHeader()
    pause_profile_endpoint = "{}/me/player/pause".format(SPOTIFY_API_URL)
    pause_request = requests.put(pause_profile_endpoint, headers=authorization_header, data=json.dumps(spotify_body))
    print(pause_request.status_code)
    if(pause_request.status_code != 204):
        pause_request.json()
    return pause_request.status_code



def getAuthorizationHeader():
    refreshCaller = Refresh()
    authorization_header = {"Authorization": "Bearer {}".format(refreshCaller.refresh())}
    return authorization_header