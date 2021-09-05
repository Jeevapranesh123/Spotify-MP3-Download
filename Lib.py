import requests
import json

with open('config.json','r') as f:
  config=json.load(f)


def apicall(playlist_id):
  url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
  token=config['OAuth_Token']
  payload={}
  headers = {
    'Authorization': 'Bearer {}'.format(token),
  }
  response = requests.request("GET", url, headers=headers, data=payload)


  return response
