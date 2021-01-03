# 最高画質YouTubeダウンローダー.py / Highest quality YouTube downloader.py



This program downloads the highest quality YouTube video. 
You have to install python.  And You have to install "Pytube" and "MoviePy".

まずpythonの開発環境を整える必要があります。
そしてPytubeとmoviepyをインストールする必要があります。


このプログラムはyoutubeのその動画の最高画質を自動で選択してダウンロードするプログラムです。


youtubeのダウンロードできるメディアにはレガシーストリームとダッシュがあります。

レガシーストリームとはビデオコーデックとオーディオコーデックの両方を備えているファイル。ただし720p以下のみです。
ダッシュとは音声無しのビデオまたはオーディオのみを備えているファイルです。


このプログラムはまず、Pytubeを使ってその動画の中の最高品質のダッシュのビデオとオーディオを選びダウンロードします。

次にmoviepyを使ってビデオとオーディオを結合し新しいファイルで出力します。

最後に結合前のビデオとオーディオを削除します。

ファイル名は動画のタイトルと同じようになるようにしています。


不具合があったらごめんなさい。
