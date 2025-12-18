import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from dotenv import load_dotenv
import os
from pathlib import Path
import pandas as pd


def run_spotify_etl():

    BASE_DIR = Path(__file__).resolve().parent
    ENV_PATH = BASE_DIR.parent / ".env"
    load_dotenv(ENV_PATH)

    # Your credentials
    CLIENT_ID = os.getenv("SPOTIFY_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_SECRET")

    # Set up Spotipy client with client credentials flow
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    ARTIST_ID = "0Y5tJX1MQlPlqiwlOH1tJY"  # Travis Scott

    albums = sp.artist_albums(ARTIST_ID, album_type="album", limit=50)
    album_ids = [a["id"] for a in albums["items"]]

    track_ids = []
    for album_id in album_ids:
        tracks = sp.album_tracks(album_id)
        for track in tracks["items"]:
            track_ids.append(track["id"])

    track_ids = list(set(track_ids))  # remove duplicates

    tracks_data = []
    for i in range(0, len(track_ids), 50):
        batch = sp.tracks(track_ids[i:i+50])
        for t in batch["tracks"]:
            tracks_data.append({
                "track_name": t["name"],
                "popularity": t["popularity"],
                "album": t["album"]["name"]
            })

    df = pd.DataFrame(tracks_data)
    top_100 = df.sort_values("popularity", ascending=False).head(100)

    top_100.to_csv("travis_scott_top_100.csv", index=False)
