import tweepy
import time

auth = tweepy.OAuthHandler('CXRgsNgtAl5AixbJiB7gUpr63', 'zRP5Hzr8vd1hWTQesNXEvLLRo2pAHo1bJYD7e2wsrhfF8EhkRY')
auth.set_access_token('1229091405152256001-1A0g6W0yIJqHCG5s0ibV3FmZk2Fy6d', '8d0yF4uj2BoL2PrrRY0TleO6akpW0XVwKT9T4NqpnAxku')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = ('covid_19', 'COVID19')
nr = 500

for tweet in tweepy.Cursor(api.search, search).items(nr):
    try:
        tweet.favorite()
        print('Liked tweet == By ' + tweet.user.screen_name)
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
        if e.reason == 'Twitter error response: status code = 429':
            time.sleep(900)
    except StopIteration:
        break



