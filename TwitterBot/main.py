import tweepy
import time

# Set up Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the bot behavior
while True:
    # Get a mention
    mentions = api.mentions_timeline()
    for mention in mentions:
        # Check if the mention is a reply to the bot
        if mention.in_reply_to_status_id_str == None:
            # Get the mention text and user info
            mention_text = mention.text
            user_screen_name = mention.user.screen_name
            user_name = mention.user.name
            
            # Process the mention
            response_text = 'Hello, @{}! Thanks for mentioning me, {}!'.format(user_screen_name, user_name)
            api.update_status(response_text, in_reply_to_status_id=mention.id)
            
    # Wait for 5 seconds before checking for new mentions
    time.sleep(5)
