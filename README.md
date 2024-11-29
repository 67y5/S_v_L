# Track Comparison Tool

A web application that compares tracks from a Spotify playlist with the songs in your local music directory. The app helps users find missing tracks in their local library, providing details like the track name and album cover. Users can search the results and easily access Spotify links to missing tracks. Built with Python, Flask, Spotipy, and HTML/CSS.

---

## Features:
- **Compare** tracks from a Spotify playlist with local music files
- **Search** through missing tracks
- **Display** track information with album covers
- **Direct Links** to Spotify for missing tracks

---

## Setup Instructions

### 1. Clone the Repository:
Start by cloning the repository to your local machine:

## 2. Install modules 
pip install Flask
pip install spotipy

### 3. Create a Spotify Developer Application:

To interact with the Spotify API, you'll need to create a **Spotify Developer** account and set up an application. Follow these steps to get your credentials:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Click **Create an App** and fill out the necessary details.
3. After creating the app, you'll be provided with your **Client ID**, **Client Secret**, and **Redirect URI**.

Once you have these credentials, update the following variables in your `app.py` with your credentials:

```python
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://localhost:8888/callback'

Replace 'your_client_id' and 'your_client_secret' with your actual Spotify Client ID and Client Secret.
Note: The Redirect URI should match the one you entered when creating your Spotify app (typically, http://localhost:8888/callback for local development).


### Key Elements:
- **Bold**: Key actions like `Spotify Developer` and **Client ID** are highlighted in bold for clarity.
- **Ordered List**: Steps are organized for easy reading.
- **Code Blocks**: The Python code is wrapped in a code block for better readability.
- **Link**: The **Spotify Developer Dashboard** is linked to for easy navigation.
- **Note**: A note is added at the end to clarify the usage of the Redirect URI.

This will result in a well-structured and easy-to-follow guide in your `README.md` when displayed on GitHub.
