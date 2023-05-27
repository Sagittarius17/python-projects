from pytube import YouTube
import os

# Step 1: Create a YouTube object with the video URL
video_url = input("Paste your video URL here-> ")
yt = YouTube(video_url)

# Step 2: Get a list of available video and audio streams
streams = yt.streams

# Step 3: Choose the stream you want to download
stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
print(stream)
# for stream in streams:
#     print(stream)

# Step 4: Download the video
output_path = os.path.join(os.path.expanduser('~'), '/path/to/local/directory')
print(f"Output path: {output_path}")
try:
    stream.download(output_path=output_path)
    print("Video downloaded successfully.")
except Exception as e:
    print("An error occurred during the download:")
    print(e)
