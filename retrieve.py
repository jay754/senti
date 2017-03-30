import tweepy
import json
import datetime
import time

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="u7x633jNJeyP2z5NHCnBj3LbQ"
consumer_secret="OWDaKKpBvkhwmLQfV4vK2SWpeu3jfdrUYrY54Pa6ZFFFLCg1QI"
access_token="606652366-r06XCAmzSDaffjg8hd3NG74dOfoEfJLjXlbGro6R"
access_token_secret="49ti9ay3ZKFd3sOjjslROjOyLPHeczl6mTIsr4RN7ew9D"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets(api, username):
    page = 1
    deadend = False
    results = []

    while True:
        try:
            tweets = api.user_timeline(username, page = page)
            for tweet in tweets:
                if (datetime.datetime.now() - tweet.created_at).days < 10:
                    #Do processing here:
                    encoded_tweet = tweet.text.encode("utf-8")
                    if "Apple" in encoded_tweet:
                        print encoded_tweet
                        results.append(encoded_tweet)
                else:
                    deadend = True
                    return results
            if not deadend:
                page+=1
                print page
                time.sleep(3)
        except Exception as e:
            print str(e)

print get_tweets(api, "Marketwatch")
