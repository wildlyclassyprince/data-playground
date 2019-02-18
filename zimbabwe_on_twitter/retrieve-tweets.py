'''
retrieve-tweets.py

The purpose of this script is to retrieve tweets from Twitter
using the Twitter API.

We will need to authenticate with the Twitter API before we can do anything else.

After which, we will then instantiate a
database connection.
'''

# Imports
import logging
import json
import tweepy
import random
import time

from pprint import pprint
from pymongo import MongoClient

# Authentication
with open('credentials.json') as creds:
    credentials = json.load(creds)

consumer_key = credentials['consumer_key']
consumer_secret = credentials['consumer_secret']
access_token = credentials['access_token']
access_token_secret = credentials['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Instantiate DB client connection
client = MongoClient()

# Create DB object
db = client.TweetDetails

# ID number generator
def id_gen():
    '''Generates random ID number.'''
    start, end = 10 ** 4, 10 ** 5
    return random.randint(start, end)

# Rate limiter
def limit_handler(cursor):
    '''Limit the number of results returned.'''
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            # Wait 5 minutes before continuing ...
            print('Wait for 5 minutes ...')
            time.sleep(5 * 60)
            print('Continuing ...')
        except StopIteration:
            break

# Query and insertion function
def search_retrieve_insert(query, number=100):
    '''Inserts data into the database.'''
    try:
        # Get the data
        for tweet in limit_handler(tweepy.Cursor(api.search)).items(number):
            # Insert data
            db.TweetDetails.insert_one({
                'id': id_gen(),
                'query': query,
                'text': tweet.text,
                'created_at': tweet.created_at,
                'full_name': tweet.author.name,
                'screen_name': tweet.author.screen_name,
                'location': tweet.author.location,
                'description': tweet.author.description,
                'source': tweet.source,
                'statuses_count': tweet.user.statuses_count,
                'retweet_count': tweet.retweet_count,
                'favorited': tweet.favorited
            })
    except Exception as e:
        print(str(e))

# Read records
def read():
    '''Reads data from the database.'''
    try:
        tweets = db.TweetDetails.find()
        for tweet in tweets:
            pprint(tweet)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    # Query and insert
    search_retrieve_insert(query='Zimbabwe', number=10000)