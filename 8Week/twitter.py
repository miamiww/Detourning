import tweepy
import json
import random
import questions

with open('creds.json', 'r') as infile:
    creds = json.load(infile)

auth = tweepy.OAuthHandler(creds['api_key'], creds['secret_key'])
auth.set_access_token(creds['access_token'], creds["secret_token"])

api = tweepy.API(auth)

results = api.search("climate change")
for r in results:
    print r.text

api.update_status('')

for r in results
possible_tweets = []

api.update_with_media(random.choice(possible_tweets))
