from __future__ import unicode_literals
import pytube
from pytube import YouTube
import youtube_dl
import os
SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '\Downloads'
def dwn(songlink):

    # print(os.getcwd())
    print(SAVE_PATH)
    link =songlink
    # yt=YouTube(link)
    # print(yt.title)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except Exception as e:
        print(e)
