import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, render_template, request

# Set your credentials here
CLIENT_ID = '31246701b6294e7792af796aa5495f05'
CLIENT_SECRET = '31176acbcfd349ef9cb283f4a8b7884a'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'playlist-read-collaborative'

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=REDIRECT_URI,
                                                scope=SCOPE))

app = Flask(__name__)

# Function to get all tracks from a Spotify playlist, handling pagination
def get_spotify_playlist_tracks(playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id, limit=100, offset=0)
    
    for item in results['items']:
        track = item['track']
        track_name = track['name']
        album_cover_url = track['album']['images'][0]['url']  # Fetch album artwork URL
        track_url = track['external_urls']['spotify']  # Fetch Spotify track URL
        tracks.append({
            'name': track_name,
            'cover_url': album_cover_url,
            'url': track_url
        })

    # Continue fetching tracks until all pages have been retrieved
    while results['next']:
        results = sp.next(results)
        for item in results['items']:
            track = item['track']
            track_name = track['name']
            album_cover_url = track['album']['images'][0]['url']  # Fetch album artwork URL
            track_url = track['external_urls']['spotify']  # Fetch Spotify track URL
            tracks.append({
                'name': track_name,
                'cover_url': album_cover_url,
                'url': track_url
            })
    
    return tracks

# Function to scan local music directory
def scan_local_music(directory):
    local_tracks = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mp3', '.flac', '.m4a')):  # Adjust file types as needed
                local_tracks.append(file.lower().replace('.mp3', '').replace('.flac', '').replace('.m4a', ''))
    return local_tracks

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        playlist_id = request.form["playlist_id"]
        local_directory = request.form["local_directory"]
        
        spotify_tracks = get_spotify_playlist_tracks(playlist_id)
        local_tracks = scan_local_music(local_directory)
        
        missing_tracks = [track for track in spotify_tracks if track['name'].lower() not in local_tracks]
        total_spotify_tracks = len(spotify_tracks)
        total_local_tracks = len(local_tracks)
        all_tracks_present = len(missing_tracks) == 0
        
        return render_template(
            "results.html",
            missing_tracks=missing_tracks,
            total_spotify_tracks=total_spotify_tracks,
            total_local_tracks=total_local_tracks,
            all_tracks_present=all_tracks_present,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
