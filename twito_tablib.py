import tablib
import tweepy


def get_all_tweets(screenName, file_type):
    consumer_key = 'JCxBbbGjvC5qIneTUJUMUQSzY'
    consumer_secret = 'vYDlU2JDXtSe5AtqHdZ1Pc2tf20ZGxU2AQvE1WD5ODIwGYrB01'
    access_token = '765174214777249792-SUPa58z6NvnxbACwexOTtYPfDVxYcSz'
    access_token_secret = 'mOWQiCjQzVXuFd0gmc1hkQh0iBGB0Biu37VvfV5eGSrPz'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    tweepy_user = tweepy.API(auth)

    alltweets = []

    screen_name = screenName

    new_tweets = tweepy_user.user_timeline(screen_name=screen_name, count=200)
    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:
        print ("getting tweets before " + str(oldest))

        new_tweets = tweepy_user.user_timeline(
            screen_name=screen_name, count=200, max_id=oldest)

        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1

        print ("..." + str(len(alltweets)) + ' tweets downloaded so far')

        # outtweets = [[tweet.id_str, tweet.created_at,
        #               tweet.text.encode("utf-8")] for tweet in alltweets]

    tweet_csv = tablib.Dataset()
    tweet_csv.headers = ["id", "created_at",
                         "text"]

    for tweet in alltweets:
        tweet_csv.append([tweet.id_str, tweet.created_at,
                          tweet.text])

    if file_type == 'CSV':
        with open('%s_tweets.csv' % screen_name, 'w') as f:
            f.write(tweet_csv.csv)

    else:
        with open("%s_tweets.xls" % screen_name, 'wb') as f:
            f.write(tweet_csv.xls)


if __name__ == '__main__':
    get_all_tweets('ValaParthvi', 'XLS')
