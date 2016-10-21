import tweepy
import csv
access_token_secret = ''
access_token = ''
consumer_secret = ''
consumer_key = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
my = api.user_timeline()

with open('tweets.csv', 'w') as csvfile:
    fieldnames = ['text', 'id', 'author', 'place', 'retweet_count', 'user']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in my:
        writer.writerow({'text': i.text, 'id': i.id, 'author': i.author.name,
                         'place': i.place, 'retweet_count': i.retweet_count, 'user': i.user.name})
