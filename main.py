import time
import os
from datetime import datetime
from search import call
from Lib import config, apicall, get_uid, get_playlists, extract_playlists
from download import dwn,SAVE_PATH
from hurry.filesize import size,si

userid = get_uid()

playlists = get_playlists(userid)

try:
    playlist_id = extract_playlists(playlists,config['Playlist'])
except Exception as e:
    print(e)
    exit(-1)

raw = {}
search = []

x = apicall(playlist_id)

if x.status_code != 200:
    print(x.json())
    exit(-1)

x = x.json()

for i in range(x['total']):
    song=x['items'][i]['track']['name']
    artist=x['items'][i]['track']['artists'][0]['name']

    raw.update({song:artist})
    search.append(song + " " + "by" + " " + artist)


start = time.time()
songs = call(search)

j = 0

for i in songs:
    link = songs[i]['link']
    dwn(link)
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



