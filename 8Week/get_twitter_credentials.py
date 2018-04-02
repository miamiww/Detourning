import tweepy
import json
# based on: https://gist.github.com/moonmilk/035917e668872013c1bd

with open('creds.json', 'r') as infile:
    creds = json.load(infile)

CONSUMER_KEY = creds['api_key']
CONSUMER_SECRET = creds['secret_key']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth_url = auth.get_authorization_url()

print 'Please authorize: ' + auth_url

verifier = raw_input('PIN: ').strip()

auth.get_access_token(verifier)

print "ACCESS_KEY = ", auth.access_token
print "ACCESS_SECRET = ", auth.access_token_secret

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'
