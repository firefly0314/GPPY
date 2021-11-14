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

inputmp4            ="/input_mp4/"
outputmp4           ="/output_mp4/"
direPASH            =os.getcwd().replace('\\','/')
tempPASH            ="/temp/"

#ファイル検索開始
files1 =glob.glob("."+inputmp4+'GX*.MP4')  #MP4を全て取得
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
    F=glob.glob("."+inputmp4+'/GX????'+str(i2)+'.MP4')#ファイル番号に関連のあるチャプター取得
    txt=open("."+tempPASH+'concat'+str(i2)+'.txt','w')#テキスト内容初期化
    bat=open("."+tempPASH+'ffmpeg'+str(i2)+'.bat','w')#batファイル内容初期化
    print("concat"+str(i2)+"reset")
    txt.close()
    bat.close()

    inputmp4temp=inputmp4.replace("/","")

    for i3 in range(len(F)):
        
        F_temp=F[i3]
        F_temp=str(F_temp)
        F_temp=F_temp.replace('./'+inputmp4temp+'\\' ,"")#MP4のファイル名抽出
        F[i3]=F_temp
        #ファイルリスト生成
        txt=open("."+tempPASH+'concat'+str(i2)+'.txt', 'a')
        txt.write("file '"+F_temp+"'\n")
        txt.close()
        #ファイル移動
        shutil.move("."+inputmp4+F_temp,"."+ tempPASH)

    #batファイル生成
    bat=open("."+tempPASH+'ffmpeg'+str(i2)+'.bat','a')
    bat.write('CD '+direPASH+tempPASH+'\n''ffmpeg -f concat -i concat'+str(i2)+'.txt -c copy '+direPASH+outputmp4+'output'+str(i2)+'.mp4 -y  \n',)
    bat.close()

    if len(F)>0: 
        print('Encode_Start')
        print(F)
        subprocess.call(direPASH+tempPASH+'ffmpeg'+str(i2)+'.bat',shell=True)#batファイル起動
        Ftmp=glob.glob("."+tempPASH+'/GX????'+str(i2)+'.MP4')#使用したファイル取得
        for i4 in range(len(F)):
            F_temp4=Ftmp[i4]
            F_temp4=str(F_temp4)
            F_temp4=F_temp4.replace('./'+tempPASH+'\\' ,"")#MP4のファイル名抽出
            shutil.move("."+tempPASH+F[i4],"."+inputmp4+"/" )#戻す
        os.remove("./"+tempPASH+'ffmpeg'+str(i2)+'.bat')
        os.remove("./"+tempPASH+'concat'+str(i2)+'.txt')
    else:
        pass
print('Finished')