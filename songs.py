import os
import subprocess
import vlc
from yt_dlp import YoutubeDL

def find_youtube_url(song_name):
    """Search for a song on YouTube and return the first result's URL."""
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "noplaylist": True,
    }
    query = f"ytsearch:{song_name}"
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        if info and 'entries' in info:
            return info['entries'][0]['url']
        else:
            return None

def play_song(url):
    """Stream and play the song using VLC."""
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(url)
    player.set_media(media)
    player.play()
    print("Playing... Press Ctrl+C to stop.")
    while True:  # Keep the script running while VLC plays
        pass

if __name__ == "__main__":
    try:
        song_name = input("Enter the song name: ")
        print("Searching for the song...")
        url = find_youtube_url(song_name)
        if url:
            print(f"Playing song from URL: {url}")
            play_song(url)
        else:
            print("Song not found. Please try another.")
    except KeyboardInterrupt:
        print("\nPlayback stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
