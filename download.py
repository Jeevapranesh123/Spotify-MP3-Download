from __future__ import unicode_literals
from pytube import YouTube
import youtube_dl
import os
from moviepy.editor import *

# SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '\Downloads'
SAVE_PATH = os.getcwd() + '/Downloads'
print(SAVE_PATH)
def dwn(songlink):

    # print(os.getcwd())
    print(SAVE_PATH)
    link =songlink
    print(link)
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

# def download_audio_with_pytube(songlink):
    # yt = YouTube(songlink)
    # audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
    # try:
    #     print(f"Downloading {yt.title} ...")
    #     audio_stream.download(output_path=SAVE_PATH)
    #     print(f"{yt.title} downloaded successfully!")
    # except Exception as e:
    #     print(f"Error downloading {yt.title}!")
    #     print(e)

def download_audio_with_pytube(songlink):
    yt = YouTube(songlink)
    audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
    
    print(f"Downloading {yt.title} ...")
    file_path = audio_stream.download(output_path=SAVE_PATH)
    
    # Convert mp4 to mp3
    audio = AudioFileClip(file_path)
    mp3_path = os.path.splitext(file_path)[0] + ".mp3"
    audio.write_audiofile(mp3_path)
    audio.close()
    
    # Optionally, remove the original mp4 file
    os.remove(file_path)
    
    print(f"{yt.title} downloaded successfully as mp3!")

import threading

# def convert_to_mp3(file_path, title):
#     # Convert mp4 to mp3
#     audio = AudioFileClip(file_path)
#     mp3_path = os.path.splitext(file_path)[0] + ".mp3"
#     audio.write_audiofile(mp3_path)
#     audio.close()
    
#     # Optionally, remove the original mp4 file
#     os.remove(file_path)
    
#     print(f"{title} converted to mp3!")

# def download_and_convert(songlink):
#     yt = YouTube(songlink)
#     audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
    
#     print(f"Downloading {yt.title} ...")
#     file_path = audio_stream.download(output_path=SAVE_PATH)
    
#     convert_to_mp3(file_path, yt.title)

#     print(f"{yt.title} downloaded successfully!")

def convert_to_mp3(file_path):
    # Convert mp4 to mp3
    audio = AudioFileClip(file_path)
    mp3_path = os.path.splitext(file_path)[0] + ".mp3"
    audio.write_audiofile(mp3_path)
    audio.close()
    
    # Optionally, remove the original mp4 file
    os.remove(file_path)

def download_audio_with_pytube(songlink):
    yt = YouTube(songlink)
    audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
    
    print(f"Downloading {yt.title} ...")
    file_path = audio_stream.download(output_path=SAVE_PATH)
    
    # Start a new thread for the conversion process
    conversion_thread = threading.Thread(target=convert_to_mp3, args=(file_path,))
    conversion_thread.start()

    print(f"{yt.title} downloaded successfully!")