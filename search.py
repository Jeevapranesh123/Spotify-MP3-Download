from pprint import pprint
from youtubesearchpython import VideosSearch
songs={}

def search(name):
    print(name)
    videosSearch = VideosSearch( name, limit = 2)
    a=videosSearch.result()

    max=0
    lp=''
    for i in range(len(a['result'])):
        m=a['result'][i]
        # print(m)
        views=m['viewCount']['text']
        v=views.split(" ")[0]
        p=int(v.replace(',',''))

        if p>max:
            max=p
            # pprint.pprint(m['link'])
            lp=m['link']
            channel=m['channel']['name']


    songs.update({name:{'channel':channel,
                 'link':lp}})


    print({name:{'channel':channel,
                 'link':lp}})

def call(dic):
    j=1
    for i in dic:
        print(" Song {} ".format(j))
        j+=1
        search(i)

        # if j==5:
        #     break

    return songs

