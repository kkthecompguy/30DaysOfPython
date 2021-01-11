
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

user = api.get_user('code')
user_timeline = user.timeline()
user_timeline_status_obj = user_timeline[0]
status_obj_id = user_timeline_status_obj.id
status_obj_screen_name = user_timeline_status_obj.user.screen_name 

api.retweet(status_obj_id)
api.create_favorite(status_obj_id)
tweet = api.get_status(status_obj_id)
tweet.user.screen_name 
api.update_status(f'@{tweet.user.screen_name}', 'Wow this is cool!', tweet.id)
 
