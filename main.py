import time
import os
from datetime import datetime
from search import call
from Lib import config, apicall, get_uid, get_playlists, extract_playlists
from download import dwn, SAVE_PATH, download_audio_with_pytube
from hurry.filesize import size, si

userid = get_uid()

playlists = get_playlists(userid)

try:
    print(config['Playlist'])
    # print(playlists)
    playlist_id = extract_playlists(playlists,config['Playlist'])
except Exception as e:
    print(e)
    # print('Invalid playlist')
    exit(-1)

raw = {}
search = []

x = apicall(playlist_id)

if x.status_code != 200:
    print(x.json())
    exit(-1)

x = x.json()

# print('Total songs in playlist: '+str(x['total']))
# for i in range(2):
#     print(i)
#     # print(x['items'])
#     song=x['items'][i]['track']['name']
#     artist=x['items'][i]['track']['artists'][0]['name']

#     raw.update({song:artist})
#     search.append(song + " " + "by" + " " + artist)


import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Spotify"]
col = db["Songs"]

data = col.find_one({"id":2})
search = data['list']

start = time.time()
songs = call(search)

j = 0

new_list = []

for i in songs:
    # new_list.append(i)
    link = songs[i]['link']
    # dwn(link)
    download_audio_with_pytube(link)
    # download_audio_ytdlp(link)
    j += 1




end=time.time()

total=end-start

print('Time taken to download: '+datetime.utcfromtimestamp(total).strftime('%H:%M:%S'))

# assing size
x = 0

# assign folder path
Folderpath = SAVE_PATH

# get size
for ele in os.scandir(Folderpath):
    x += os.stat(ele).st_size

print('Download Size:'+size(x, system=si))
