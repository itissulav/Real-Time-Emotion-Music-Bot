import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your app credentials
CLIENT_ID = '520652e7ee434801ae4760e263a023eb'
CLIENT_SECRET = '75d85eb351034275959de6d1598c6a40'
REDIRECT_URI = 'http://127.0.0.1:8080/callback'

# Scope needed to read recently played tracks
SCOPE = "user-read-playback-state user-modify-playback-state user-library-read streaming"

def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        show_dialog=True,
        cache_path=None
    ))
    return sp