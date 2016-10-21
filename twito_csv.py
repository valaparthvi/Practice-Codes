import tweepy
import csv
access_token_secret = 'mOWQiCjQzVXuFd0gmc1hkQh0iBGB0Biu37VvfV5eGSrPz'
access_token = '765174214777249792-SUPa58z6NvnxbACwexOTtYPfDVxYcSz'
consumer_secret = 'vYDlU2JDXtSe5AtqHdZ1Pc2tf20ZGxU2AQvE1WD5ODIwGYrB01'
consumer_key = 'JCxBbbGjvC5qIneTUJUMUQSzY'

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
