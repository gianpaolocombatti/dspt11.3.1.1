import tweepy
import os
from twitter_app.twitter_data_model import DB, Tweet, User

twitter_auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_KEY_SECRET'])
twitter_api = tweepy.API(twitter_auth)

nlp
