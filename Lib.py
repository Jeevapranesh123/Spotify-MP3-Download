import requests
import pprint
import json

with open('config.json','r') as f:
  config=json.load(f)


def apicall(playlist_id):

    # url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
    url = "https://api.spotify.com/v1/playlists/2jcfUb5ix3GwWtLMv4EqQq/tracks?offset=200&limit=100"
    token=config['OAuth_Token']
    payload={}
    headers = {
      'Authorization': 'Bearer {}'.format(token),
    }
    print(url)
    response = requests.request("GET", url, headers=headers, data=payload)

    return response


def get_uid():
    profile=config['profile_url']
    a = profile[30:]
    uid = ''
    for i in a:
      if i == '?':
        break
      uid = uid + i

    return uid


def get_playlists(userid):

    url = "https://api.spotify.com/v1/users/{}/playlists?offset=0&limit=20".format(userid)

    payload = {}
    headers = {
      'Authorization': 'Bearer {}'.format(config['OAuth_Token'])
      }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def extract_playlists(playlists_json,playlists_wanted):

    for i in range(len(playlists_json['items'])):
        print(playlists_json['items'][i]['name'])
        # print(playlists_json)
        # print("\n")
        p = config['Playlist'].split('?')

        pprint.pprint(playlists_json['items'][i]['external_urls']['spotify'])
        if p[0]==playlists_json['items'][i]['external_urls']['spotify']:
            playlist_id=playlists_json['items'][i]['id']
            print(playlist_id)
            return playlist_id

    raise Exception('Invalid playlist')


