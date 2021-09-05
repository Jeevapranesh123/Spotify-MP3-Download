import time
from datetime import datetime
import os
from search import call
from Lib import config,apicall
from download import dwn,SAVE_PATH
# from hurry.filesize import size



raw={}
search=[]
x=apicall(config['playlist_id'])

if x.status_code!=200:
    print(x.json())
    exit(-1)

x=x.json()

for i in range(x['total']):
    song=x['items'][i]['track']['name']
    artist=x['items'][i]['track']['artists'][0]['name']

    raw.update({song:artist})
    search.append(song + " " + "by" + " " + artist)

starttime=time.time()
songs=call(search)
j=0

for i in songs:
    link=songs[i]['link']
    dwn(link)
    j+=1

endtime=time.time()

timetaken=endtime-starttime

print(datetime.utcfromtimestamp(timetaken).strftime('%H:%M:%S'))

# assing size
size = 0

# assign folder path
Folderpath = SAVE_PATH

# get size
for ele in os.scandir(Folderpath):
    size += os.stat(ele).st_size

print(size)