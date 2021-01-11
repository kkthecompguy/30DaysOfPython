#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from urllib.parse import urlencode
from urllib.parse import urlparse, parse_qsl


# In[2]:


GOOGLE_API_KEY = 'AIzaSyCigKo_qdgK82NOWQNOhUcltn_ELubfD00' 


# In[7]:


class GoogleMapsClient(object):
    lat = None
    long = None
    data_type = 'json'
    location_query = None
    api_key = None
    
    def __init__(self, api_key=None,  address_or_postal_code=None, *args, **kwargs):
        self.api_key = api_key
        if self.api_key == None:
            raise Exception("API Key is required") 
        self.location_query = address_or_postal_code 
        if self.location_query != None:
            self.extract_lat_long()
    
    def extract_lat_long(self, location=None):
        loc_query = self.location_query
        if location != None:
            loc_query = location
        params = {'address': loc_query, 'key': self.api_key}
        url_params = urlencode(params)
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        url = f'{endpoint}?{url_params}'
        r = requests.get(url)
        latlong = {}
        if r.status_code in range(200, 299):
            latlong =  r.json()['results'][0]['geometry']['location']
            try:
                lat, long =  latlong.get('lat'), latlong.get('lng')
                self.lat = lat
                self.long = long
                return lat, long
            except:
                pass
        return {}
    
    def search(self, keyword="Mexican Food", location=None, radius=1000):
        endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/{self.data_type}"
        lat, long = self.lat, self.long
        if location != None:
            lat, long = self.extract_lat_long(location=location)
        params  = {
            'key': self.api_key,
            'location': f'{lat},{long}', 
            'radius': radius,
            'keyword': keyword
        } 
        params_encoded = urlencode(params)
        url = f"{endpoint}?{params_encoded}"
        r = requests.get(url) 
        if r.status_code in range(200, 299):
            return r.json()
        return {}
        
        
    def detail(self, place_id='ChIJN1t_tDeuEmsRUsoyG83frY4'): 
        detail_base_url = "https://maps.googleapis.com/maps/api/place/details/json"
        detail_params = {
            'place_id': place_id,
            'key': self.api_key,
            'fields' : 'formatted_address,name,geometry,place_id'
        } 
        details_params_encoded = urlencode(detail_params)
        url = f'{detail_base_url}?{details_params_encoded}' 
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return {}


# In[9]:


client = GoogleMapsClient(api_key=GOOGLE_API_KEY, address_or_postal_code="1600 Amphitheatre Parkway, Mountain View, CA") 


# In[11]:


client.search(keyword="Tacos", location="Nairobi, KE")


# In[12]:


client.detail(place_id="ChIJeWxtoAgRLxgRDHNAsinTDaE")


# In[ ]:




