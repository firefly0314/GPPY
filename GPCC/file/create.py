import os
import glob

def DirectoryCreate(dirPASH):
    dirTF=os.path.isdir("."+dirPASH)
    if dirTF == True:
        pass
    else:
        os.makedirs("."+dirPASH)
    return dirTF


