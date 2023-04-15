from pytube import YouTube

# Step 1: Create a YouTube object with the video URL
video_url = input("Paste your video URL here-> ")
yt = YouTube(video_url)

# Step 2: Get a list of available video and audio streams
streams = yt.streams

# Step 3: Choose the stream you want to download
stream = yt.streams.filter(only_video=True).order_by('resolution').desc().first()

for stream in streams:
    print(stream)

# Step 4: Download the video
stream.download(output_path='/path/to/save/directory')


