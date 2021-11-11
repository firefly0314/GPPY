import glob
import os
import subprocess
import shutil
#初期化
files1=[]
Flen=0
Mlis=[]
Jlis=[]
F2=[]
F=[]

#ファイル検索開始
files1 =glob.glob('./mp4/GX*.MP4')  #MP4を全て取得
print(len(files1),'Files')          #ファイル数取得
for i in range(len(files1)):
    Flen=files1[i]
    Mlis.append(int(Flen[-8:-4]))   #ファイルネーム格納
    Jlis.append(int(Flen[-10:-8]))  #チャプター番号格納
#データ整理、ソート&重複削除
Mlis.sort()
Mlistemp=set(Mlis)
Mlis=list(Mlistemp)
Jlis.sort()
list(set(Jlis))
Jlistemp=set(Jlis)
Jlis=list(Jlistemp)

print('M',max(Mlis),"~",min(Mlis))#ファイルネーム表示
mi=min(Mlis)
mx=max(Mlis)+1
for i2 in range(mi,mx):#ファイルの数分ループ処理
    F=glob.glob('./mp4/GX????'+str(i2)+'.MP4')#ファイル番号に関連のあるチャプター取得
    txt=open('mp4/concat'+str(i2)+'.txt','w')#テキスト内容初期化
    bat=open('ffmpeg'+str(i2)+'.bat','w')#batファイル内容初期化
    print("concat"+str(i2)+"reset")
    txt.close()
    bat.close()

    for i3 in range(len(F)):
        
        F_temp=F[i3]
        F_temp=str(F_temp)
        F_temp=F_temp.replace('./mp4\\' ,"")
        F[i3]=F_temp
        #ファイルリスト生成
        txt=open('mp4/concat'+str(i2)+'.txt', 'a')
        txt.write("file '"+F_temp+"'\n")
        txt.close()

    print("concat"+str(i2)+"completed")
    print("Encode"+str(i2)+"Start")
    #batファイル生成
    bat=open('ffmpeg'+str(i2)+'.bat','a')
    bat.write('cd D:\gppy\mp4\n''ffmpeg -f concat -i concat'+str(i2)+'.txt -c copy output'+str(i2)+'.mp4 -y\n',)
    bat.close()

    if len(F)>0: 
        print('Encode_Start')
        print(F)
        subprocess.call('ffmpeg'+str(i2)+'.bat',shell=True)#batファイル起動
    else:
        pass
print('Finished')