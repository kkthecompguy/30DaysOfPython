
import tweepy
import webbrowser
import time
import pandas as pd

consumer_key = "SRKYbF44wb7ImB9c3XxppcX22"
consumer_secret = "GUZpAdVN31FRnD5Tjaxqk5l4tvMlQq6pGl01H7ThhwzVr6yRlV"
callback_uri = "oob"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
request_url = auth.get_authorization_url()
webbrowser.open(request_url)
user_pin_input = input("What is the user pin? ")
auth.get_access_token(user_pin_input)

api = tweepy.API(auth) 

for i, status in enumerate(tweepy.Cursor(api.home_timeline).items(50)):
    print(i, status.text)

for i, status in enumerate(tweepy.Cursor(api.user_timeline, screen_name='crazyelvo').items(50)):
print(i, status.text)

cfe_friends_ids = []
for i, _id in enumerate(tweepy.Cursor(api.friends_ids, screen_name='joincfe').items(50)):
    cfe_friends_ids.append(_id)
    
query = '#django -JQuery'
for i, status in enumerate(tweepy.Cursor(api.search, q=query).items(50)):
    print(i, status.text, status.author.screen_name)
    

def handle_limit(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            # send email, webhook, logs
            time.sleep(15 * 60)
for i, status in enumerate(handle_limit(tweepy.Cursor(api.search, q=query).items(50))):
