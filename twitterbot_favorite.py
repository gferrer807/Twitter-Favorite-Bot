import tweepy
from time import sleep
from credentials import *
import twitter
import sys
import os
import random

#verify credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#search for tweets to favorite according to timeline
for tweet in tweepy.Cursor(api.home_timeline, result_type='recent').items(12):
    try:

        #time should be random to avoid breaking twitters automation rule
        time_ref = random.randint(300,600)

        #print username for tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        #favorite tweet
        tweet.favorite()
        print('Succsesfully favorited the tweet')
        sleep(time_ref)

        
    #indicate if the tweet was already liked
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(1200)

    #stop program once max items has been reached
    except StopIteration:
        break

#restart the program
os.execv(sys.executable, ['python'] + sys.argv)
