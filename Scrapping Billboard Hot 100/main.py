import requests
from bs4 import BeautifulSoup
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint


user_year = input("What year would you like to travel to? Type the date in the format YYYY-MM-DD: ")
client_id = "d3c8858f40004eaabbe8e0c63d859973"
client_secret = "6fe18714c77c428187eb793858444c26"
scope = "playlist-modify-private"
url = f"https://www.billboard.com/charts/hot-100/{user_year}/"
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}


response= requests.get(url,headers=headers)
songs = response.text

soup = BeautifulSoup(songs,"html.parser")
song = soup.find_all("h3", class_="c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max")
song_list = [music.getText().strip() for music in song]

authentication = SpotifyOAuth(client_id=client_id, client_secret=client_secret,redirect_uri="https://example.org/callback"
                              , scope=scope, username="gha_bby")


year = user_year.split("-")[0]
sp = spotipy.Spotify(auth_manager=authentication)
user_id = sp.current_user()["id"]
track_UIs= []
for song in song_list:
    result= sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        track_UIs.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id,name=f"{user_year} Billboard 100", public=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=track_UIs)
print(song_list)
print(playlist["name"])
print(playlist["external_urls"]["spotify"])
