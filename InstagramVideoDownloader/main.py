import instaloader

def download_instagram_video(url):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Retrieve metadata for the specified URL
        post = instaloader.Post.from_shortcode(loader.context, url)
        
        # Download the video
        loader.download_post(post, target='#downloaded_videos')
        
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error occurred:", str(e))

# Example usage
video_url = 'https://www.instagram.com/reel/CrCBPd3OySG/'
download_instagram_video(video_url)
