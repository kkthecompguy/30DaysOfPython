import requests

ngrok_url = 'https://6aa2470f3c25.ngrok.io'
endpoint = '/box-office-mojo'
url = f'{ngrok_url}{endpoint}'

r = requests.get(url)
if r.status_code == 200:
  print(r.text)