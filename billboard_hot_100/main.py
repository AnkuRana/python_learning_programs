from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

billboard_url = "https://www.billboard.com/charts/hot-100/"
get_date = input("Enter date of your interest yyyy-mm-dd: ")
#
updated_BB_url = billboard_url + get_date
get_date = get_date.split("-")[0]
bb_data = requests.get(updated_BB_url)
bb_data.raise_for_status()

# using beautiful soap api to get information from billboard
soup = BeautifulSoup(bb_data.text, "html.parser")

all_song_div = soup.find_all(name="div", class_="o-chart-results-list-row-container")
playlist = []
song_uris = []

for index in range(len(all_song_div)):
    playlist.append(all_song_div[index].find('h3').getText().strip())

# getting the client key from env
cl_id = os.environ.get("cl_id")
cl_key = os.environ.get("cl_key")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cl_id,
                                               client_secret=cl_key,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private", cache_path="token.txt"))
# getting spotify user id
spotify_user_id = sp.me()["id"]
# playlistid = sp.user_playlist_create(user=spotify_user_id, name="bbTimeMachine", description="billlboard songs from particular date "
#                                                                                  "created by python", public=False)

playlistid = "6ovDvTB6DPEuA8ck6eGiBC"
for song in playlist:
    try:
        search_song = sp.search(q=f"track:{song} year:{get_date}", type="track", limit=1)
        song_uris.append(search_song["tracks"]["items"][0]["id"])
    except IndexError:
        print(f"Song: {song} not found.")

sp.playlist_add_items(playlist_id=playlistid, items=song_uris)
