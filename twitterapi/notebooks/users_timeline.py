
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

def extract_timeline_as_df(timeline_list):
    columns = set()
    allowed_types = [str, int]
    tweets_data = []
    for status in timeline_list:
        status_dict = dict(vars(status))
        keys = status_dict.keys()
        single_tweet_data = {'user': status.user.screen_name, 'author': status.author.screen_name}
        for k in keys: 
            try:
                v_type = type(status_dict[k])
            except:
                v_type = None
            if v_type != None:
                if v_type in allowed_types:
                    columns.add(k)
                    single_tweet_data[k] = status_dict[k]
        tweets_data.append(single_tweet_data)

    header_cols = list(columns)
    header_cols.append('user')
    header_cols.append('author')
    df = pd.DataFrame(tweets_data, columns=header_cols)
    return df

user = api.get_user('code') 
user_timeline = user.timeline()
df2 = extract_timeline_as_df(user_timeline)
df2.head()
