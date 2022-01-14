import glob
import os
import subprocess
import shutil
#import tqdm
import yaml
#my Librarys↓
from GPCC import *
import GPCC

#初期化
F2=[]
F=[]

with open('config.yaml', 'r') as yml:
    config = yaml.safe_load(yml)

#デフォルトの値です
inputmp4            ="/input_mp4/"
Finished_using      ="/Finished_using/"
outputmp4           ="/output_mp4/"
tempPASH            ="/temp/"
direPASH            =os.getcwd().replace('\\','/')
loglevel            =24
stats               ='-y'
#デフォルトをオーバーライド
inputmp4            =str(config.get('inputmp4'))
Finished_using      =str(config.get('Finished_using'))
outputmp4           =str(config.get('outputmp4'))
tempPASH            =str(config.get('tempPASH'))
loglevel            =str(config.get('loglevel'))
stats               =str(config.get('stats'))
#ディレクトリが存在しない場合作成します
GPCC.DirectoryCreate(tempPASH)   

GPCC.DirectoryCreate(inputmp4)

GPCC.DirectoryCreate(outputmp4)

GPCC.DirectoryCreate(Finished_using)

#ファイル検索開始
mx, mi =GPCC.filename(inputmp4)

    #メインループ
for i2 in range(mi,mx):#ファイルの数分ループ処理

    

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
    bat.write('CD '+direPASH+tempPASH+'\n''ffmpeg -f concat -i concat'+str(i2)+'.txt -c copy -analyzeduration 256M -probesize 256M '+direPASH+outputmp4+'output'+str(i2)+'.mp4 -loglevel '+loglevel+' -stats '+stats+'\n')
    bat.close()

    if len(F)>0: 
        print('Encode_Start')
        print(F)
        #subprocess.run(direPASH+tempPASH+'ffmpeg'+str(i2)+'.bat',shell=True)#batファイル起動
        Ftmp=glob.glob("."+tempPASH+'/GX????'+str(i2)+'.MP4')#使用したファイル取得
        Ftmp=glob.glob("."+tempPASH+'/GX???'+str(i2)+'.MP4')#使用したファイル取得
        for i4 in range(len(F)):
            
            if len(F)==1:
                shutil.move("."+tempPASH+F[i4],"."+Finished_using+"/" )#戻す    
            else:
                F_temp4=Ftmp[i4]
                F_temp4=str(F_temp4)
                F_temp4=F_temp4.replace('./'+tempPASH+'\\' ,"")#MP4のファイル名抽出
                shutil.move("."+tempPASH+F[i4],"."+Finished_using+"/" )#戻す

        os.remove("./"+tempPASH+'ffmpeg'+str(i2)+'.bat')
        os.remove("./"+tempPASH+'concat'+str(i2)+'.txt')
    else:
        pass
else:
    print("no_import_files")
print('Finished')

os.system('PAUSE')