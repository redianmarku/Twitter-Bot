import tweepy
import time

auth = tweepy.OAuthHandler('d8WirUTs1raLqcssfwoVGGjrJ', 'MKTxvjfuwifknQiqaN6QI9Y2wuGDr0s9oXvht51xb18aNhRrst')
auth.set_access_token('711493306228854785-D17crM3KMUZ9QwBj6wj505XmzkeU9kp', 'khChYKihHaZa0tqPwzl9DdcGnnTqQE8EyG8O3NeegNNfC')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '#100DaysOfCode'
nr = 500

for tweet in tweepy.Cursor(api.search, search).items(nr):
    try:
        tweet.favorite()
        print('Liked tweet == By ' + tweet.user.screen_name)
        time.sleep(15)
    except tweepy.TweepError as e:
        print(e.reason)
        if e.reason == 'Twitter error response: status code = 429':
            time.sleep(900)
    except StopIteration:
        break



