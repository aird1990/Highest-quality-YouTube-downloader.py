# You have to install "Python". And You have to install "Pytube".
# url = ' '  　←YouTube URL
# download_folder = ' '   ←Download folder path

# 注意 事前にPythonをインストールする必要があります。またPytubeもインストールする必要があります。
# urlのところにダウンロードしたい動画のurlを張ってください
# download_folderのところにダウンロードしたいところのフォルダのパスを張ってください
import pytube
url = 'https://www.youtube.com/watch?v=QDX-1GuF2Gs'
download_folder = 'C:/Users/AIR-D/Desktop'

format_list2 = pytube.YouTube(url).streams.filter(mime_type='audio/mp4').first().download(download_folder)
