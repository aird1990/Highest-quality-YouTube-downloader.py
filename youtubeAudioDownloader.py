# This program downloads youtube audio/mp4 files. And convert mp4 to mp3.

# Attention, please!
# First of all, you have to install "Python". And You have to install "Pytube"and "MoviePy".

# url = ' '  　←YouTube URL
# download_folder = ' '   ←Download folder path

# このプログラムは、YouTubeのaudio/mp4ファイルをダウンロードします。そしてmp4をmp3に変換します。
# 注意 事前にPythonをインストールする必要があります。またPytubeもmoviepyもインストールする必要があります。
# url = ' ' のところにダウンロードしたい動画のurlを張ってください
# download_folder = ' ' のところにダウンロードしたいところのフォルダのパスを張ってください。その2行以外はいじらなくて大丈夫です。

import pytube
url = 'https://www.youtube.com/watch?v=QDX-1GuF2Gs'
download_folder = 'C:/Users/AIR-D/Desktop'


format_list2 = pytube.YouTube(url).streams.filter(mime_type='audio/mp4').first().download(download_folder)

import os

os.chdir(download_folder)
print(os.getcwd())

import moviepy.editor as mp

mp4_file = pytube.YouTube(url).title + '.mp4'
mp3_file = pytube.YouTube(url).title + '.mp3'

clip = mp.AudioFileClip(mp4_file)
clip.write_audiofile(mp3_file)
clip.close()

os.remove(mp4_file)
