import json
from flask import Flask, request, redirect, session
import requests
import json
from urllib.parse import quote

app = Flask(__name__)
app.secret_key = "super secret key"

# Authentication Steps, paramaters, and responses are defined at https://developer.spotify.com/web-api/authorization-guide/
# Visit this url to see all the steps, parameters, and expected response.

#  Client Keys
CLIENT_ID = ""
CLIENT_SECRET = ""

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Server-side Parameters
CLIENT_SIDE_URL = "http://localhost"
PORT = 5000
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPE = "playlist-modify-public playlist-modify-private streaming user-read-playback-state"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}


@app.route("/")
def index():
    # Auth Step 1: Authorization
    url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)


@app.route("/callback")
def callback():
    # Auth Step 4: Requests refresh and access tokens
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(post_request.text)

    session['access_token'] = response_data["access_token"]
    session['refresh_token'] = response_data["refresh_token"]
    session['expires_in'] = response_data["expires_in"]

    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    # print(access_token)
    # print(refresh_token)
    # print(expires_in)

    return ''

@app.route("/play")
def play():
    
    authorization_header = getAuthorizationHeader()

    body = {
        "context_uri": "spotify:playlist:5XCRfaXW22GIQIZrUrw2gc",
        "offset": {
            "position": 6
        },
        "position_ms": 0
        }

    # Auth Step 6: Use the access token to access Spotify API
    play_endpoint = "{}/me/player/play".format(SPOTIFY_API_URL)

    play_request = requests.put(play_endpoint, headers=authorization_header, data=json.dumps(body))
    # print(play_request.json())
    return 'play_request.status_code'

@app.route("/pause")
def pause():
    authorization_header = getAuthorizationHeader()

    pause_profile_endpoint = "{}/me/player/pause".format(SPOTIFY_API_URL)
    pause_request = requests.put(pause_profile_endpoint, headers=authorization_header)
    print((pause_request.status_code))
    return 'pause_request.status_code'

@app.route("/next")
def next():
    authorization_header = getAuthorizationHeader()

    pause_profile_endpoint = "{}/me/player/devices".format(SPOTIFY_API_URL)
    pause_request = requests.get(pause_profile_endpoint, headers=authorization_header)
    print((pause_request.json()))
    return 'pause_request.status_code'

def refreshAccessToken():
    print('yea')

def getAuthorizationHeader():
    authorization_header = {"Authorization": "Bearer {}".format(session['access_token'])}
    return authorization_header


if __name__ == "__main__":
    app.run(debug=True, port=PORT)