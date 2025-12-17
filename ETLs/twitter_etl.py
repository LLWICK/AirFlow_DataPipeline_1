import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR.parent / ".env"
load_dotenv(ENV_PATH)


Twitter_Api_key = os.getenv("Twitter_API_Key")
Twitter_secret_key = os.getenv("Twitter_secret")
Access_token = os.getenv("Access_Token")
Access_token_secret = os.getenv("Access_Token_Secret")
bearer_token = os.getenv("BEARER_TOKEN")

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=Twitter_Api_key,
    consumer_secret=Twitter_secret_key,
    access_token=Access_token,
    access_token_secret=Access_token_secret,
)

user = client.get_user(username="elonmusk")

ELON_USER_ID = "44196397"  # hard-coded

tweets = client.get_users_tweets(
    id=ELON_USER_ID,
    max_results=10,
    tweet_fields=["created_at", "public_metrics"]
)

tweet_list = []

if tweets.data:
    for tweet in tweets.data:
        refined_tweet = {
            "user": "elonmusk",
            "text": tweet.text,
            "like_count": tweet.public_metrics["like_count"],
            "retweet_count": tweet.public_metrics["retweet_count"],
            "created_at": tweet.created_at
        }

        tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv("../data/elon_tweets.csv", index=False)


