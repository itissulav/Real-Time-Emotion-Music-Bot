# spotify_player.py
from spotipy import Spotify

import webbrowser

def play_song(title, artist, sp):
    """
    Search for the song on Spotify using title and artist,
    then open the song's Spotify web player URL in the default browser.
    
    Args:
        title (str): Song title.
        artist (str): Artist name.
        sp (spotipy.Spotify): Authenticated Spotify client.
    """
    query = f"track:{title} artist:{artist}"
    results = sp.search(q=query, type='track', limit=1)
    tracks = results.get('tracks', {}).get('items', [])
    
    if not tracks:
        print("No matching song found on Spotify.")
        return
    
    track = tracks[0]
    spotify_url = track['external_urls']['spotify']  # Web URL for the song
    
    print(f"Opening Spotify URL: {spotify_url}")
    webbrowser.open(spotify_url)
