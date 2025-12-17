import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from dotenv import load_dotenv
import os
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR.parent / ".env"
load_dotenv(ENV_PATH)

# Your credentials
CLIENT_ID = os.getenv("SPOTIFY_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_SECRET")

# Set up Spotipy client with client credentials flow
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

tracks = sp.artist_top_tracks("0Y5tJX1MQlPlqiwlOH1tJY")  

rows = []
for track in tracks["tracks"]:
    rows.append({
        "track_name": track["name"],
        "popularity": track["popularity"],
        "duration_ms": track["duration_ms"],
        "release_date": track["album"]["release_date"]
    })

df = pd.DataFrame(rows)
df.to_csv("./data/travisScott_top_tracks.csv", index=False)
