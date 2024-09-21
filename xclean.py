import tweepy

API_KEY = '#'
API_SECRET_KEY = '#'
ACCESS_TOKEN = '#'
ACCESS_TOKEN_SECRET = '#'

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

with open('id.txt', 'r') as file:
    tweet_ids = file.readlines()

for tweet_id in tweet_ids:
    tweet_id = tweet_id.strip()
    try:
        api.destroy_status(tweet_id)
        print(f"Tweet {tweet_id} successfully deleted.")
    except tweepy.TweepyException as e:
        print(f"Error deleting tweet {tweet_id} : {e}")

