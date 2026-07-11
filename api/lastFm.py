import os
import requests
from dotenv import load_dotenv
from colorama import Fore
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")
USERNAME = input("User (default=qbqt): ") or "qbqt"

def lastfm_request(method, **params):
    params.update({
        "method": method,
        "user": USERNAME,
        "api_key": API_KEY,
        "format": "json"
    })

    response = requests.get("https://ws.audioscrobbler.com/2.0/", params=params)
    response.raise_for_status()
    return response.json()

def show_recents():

    print("=== Recently Played ===")

    i = 1

    for track in recent["recenttracks"]["track"]:
        artist = track["artist"]["#text"]
        name = track["name"]
        if "@attr" in track and track["@attr"].get("nowplaying") == "true":
            pass
        else:
            print(f"{i}. {Fore.CYAN}\"{name}\"{Fore.RESET} by {Fore.MAGENTA}\"{artist}\"{Fore.RESET}")
            i = i + 1

def show_artists():

    print("=== Top Artists ===")

    for i, artist in enumerate(artists["topartists"]["artist"], start=1):
        print(f"{i}. {Fore.CYAN}\"{artist['name']}\"{Fore.RESET} ({Fore.MAGENTA}{artist['playcount']} plays{Fore.RESET})")

def show_tracks():

    print("=== Top Tracks ===")

    for i, track in enumerate(tracks["toptracks"]["track"], start=1):
        print(f"{i}. {Fore.CYAN}\"{track['name']}\"{Fore.RESET} by {Fore.MAGENTA}\"{track['artist']['name']}\"{Fore.RESET} ({Fore.LIGHTBLUE_EX}{track['playcount']} plays{Fore.RESET})")

def main():
    user = lastfm_request("user.getInfo")
    print("\033[H\033[J", end="")
    print(f"@{user["user"]['realname']} ({Fore.LIGHTRED_EX}https://www.last.fm/user/{user["user"]['name']}{Fore.RESET}):")

    track = recent["recenttracks"]["track"][0]

    artist = track["artist"]["#text"]
    name = track["name"]

    if "@attr" in track and track["@attr"].get("nowplaying") == "true":
        print(f"\n{Fore.LIGHTGREEN_EX}Online:{Fore.RESET} Listening to {Fore.CYAN}\"{name}\"{Fore.RESET} by {Fore.MAGENTA}\"{artist}\"{Fore.RESET}")
    else:
        print(f"\n{Fore.RED}Offline:{Fore.RESET} Last listened to {Fore.CYAN}\"{name}\"{Fore.RESET} by {Fore.MAGENTA}\"{artist}\"{Fore.RESET}")

print(f"Fetching user info for {lastfm_request("user.getInfo")["user"]['name']} ({lastfm_request("user.getInfo")["user"]['realname']})")

while True:
    recent = lastfm_request("user.getRecentTracks", limit=10)
    tracks = lastfm_request("user.getTopTracks", period="overall", limit=10)
    artists = lastfm_request("user.getTopArtists", period="overall", limit=10)

    time.sleep(1)

    main()
    print("")
    show_recents()
    print("")
    show_tracks()
    print("")
    show_artists()
