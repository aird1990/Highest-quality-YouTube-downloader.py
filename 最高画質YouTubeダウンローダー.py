# 注意 事前にPytubeとmoviepyをインストールする必要があります。
# urlのところにダウンロードしたい動画のurlを張ってください
# download_folderのところにダウンロードしたいところのフォルダのパスを張ってください
import pytube
url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
download_folder = 'C:/Users/AIR-D/Desktop'


# 音声ダウンロード　
format_list2 = pytube.YouTube(url).streams.filter(mime_type='audio/mp4').first().download(download_folder)

import os

os.chdir(download_folder)
print(os.getcwd())

path1 = pytube.YouTube(url).title + '.mp4'
path2 = pytube.YouTube(url).title + '2.mp4'

os.rename(path1, path2)

# 一番解像度の高い映像ファイルをダウンロード
format_list1 = pytube.YouTube(url).streams.filter(mime_type='video/mp4').order_by('resolution').desc().first().download(download_folder)

path3 = pytube.YouTube(url).title + '.mp4'
path4 = pytube.YouTube(url).title + '3.mp4'

os.rename(path3, path4)

# 映像ファイルと音声ファイルを結合して、出力ファイルを書き出し
import moviepy.editor as mp

clip = mp.VideoFileClip(path4).subclip()
clip.write_videofile(path3, audio=path2)

# 音声ファイルと映像ファイルを削除
os.remove(path2)
os.remove(path4)
