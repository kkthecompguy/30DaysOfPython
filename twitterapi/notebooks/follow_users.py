
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
user_friends = user.followers()

my_new_friends = []
for friend in user_friends:
    my_new_friends.append(friend.screen_name)
    relationship = api.create_friendship(friend.screen_name)
    
for friend in my_new_friends:
    api.destroy_friendship(friend))
 
