# You have to install "Pytube" and "MoviePy".
# url = ' '  　←YouTube URL
# download_folder = ' '   ←Download folder path
import pytube
url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
download_folder = 'C:/Users/AIR-D/Desktop'


# Download audio/mp4
format_list2 = pytube.YouTube(url).streams.filter(mime_type='audio/mp4').first().download(download_folder)

import os

os.chdir(download_folder)
print(os.getcwd())

path1 = pytube.YouTube(url).title + '.mp4'
path2 = pytube.YouTube(url).title + '2.mp4'

os.rename(path1, path2)

# Download Highest quality video/mp4
format_list1 = pytube.YouTube(url).streams.filter(mime_type='video/mp4').order_by('resolution').desc().first().download(download_folder)

path3 = pytube.YouTube(url).title + '.mp4'
path4 = pytube.YouTube(url).title + '3.mp4'

os.rename(path3, path4)

# Merge video/mp4 with audio/mp4
import moviepy.editor as mp

clip = mp.VideoFileClip(path4).subclip()
clip.write_videofile(path3, audio=path2)

# Delete video/mp4 and audio/mp4
os.remove(path2)
os.remove(path4)
