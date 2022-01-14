import os
import glob

def Chapter(inputmp4):
    chapter=[]
    files =glob.glob("."+inputmp4+'GX*.MP4')  #MP4を全て取得
    for i in range(len(files)):
        Flen=files[i]
        chapter.append(int(Flen[-10:-8]))  #チャプター番号格納
    chapter.sort
    chapter=set(chapter)
    max=max(chapter)
    min=min(chapter)
    return max, min
    


def filename(inputmp4):
    files=[]
    files =glob.glob("."+inputmp4+'GX*.MP4')  #MP4を全て取得
    for i in range(len(files)):
        Flen=files[i]
        files.append(int(Flen[-8:-4]))  #チャプター番号格納
    files.sort
    files=set(files)
    max=max(files)
    min=min(files)
    return max, min, files