import os
import requests
import pandas as pd


api_key_v3 = '32dfea6359b57a648549c4baad6707cf'
api_key_v4 ='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMmRmZWE2MzU5YjU3YTY0ODU0OWM0YmFhZDY3MDdjZiIsInN1YiI6IjVlYTAyMjM5MDdmYWEyMDAxYWZhNGFlMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hT89VlsArMNEKYrBJxr7o2tcD-SA-dXgpNHtJk50m1w'
api_version = 4
api_base_url = f'https://api.themoviedb.org/{api_version}'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


headers = {
  'Authorization': f'Bearer {api_key_v4}',
  'Content-Type': 'application/json;charset=utf-8'
}
# endpoint = f'{api_base_url}{endpoint_url}?api_key={api_key}'


def get_movie_ids(api_base_url, headers, search_query):
  search_resource_url = '/search/movie'
  endpoint = f'{api_base_url}{search_resource_url}?query={search_query}'

  movie_ids = set()
  r = requests.get(endpoint, headers=headers)
  if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
      for result in results:
        _id = result['id']
        movie_ids.add(_id)
  return list(movie_ids)


def get_movie_by_id(movie_id):
  endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=32dfea6359b57a648549c4baad6707cf'

  r = requests.get(endpoint)
  if r.status_code in range(200, 299):
    movie_data = r.json()
  return movie_data


search_query = input('Enter the name of the movie \n')
movie_ids = get_movie_ids(api_base_url, headers, search_query)
movies_data = []
for movie_id in movie_ids:
  movie_dict = get_movie_by_id(movie_id)
  movies_data.append(movie_dict)

def movie_data_csv(movies_data, search_query):
  filepath = os.path.join(BASE_DIR, 'movies')
  os.makedirs(filepath, exist_ok=True)
  name = search_query.strip().replace(' ', '_')
  output = os.path.join(filepath, f'{name}.csv')
  df = pd.DataFrame(movies_data)
  df.to_csv(output, index=False)


movie_data_csv(movies_data, search_query)