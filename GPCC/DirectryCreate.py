import os

def dc(dirPASH):
    dirTF=os.path.isdir("."+dirPASH)
    if dirTF == True:
        pass
    else:
        os.makedirs("."+dirPASH)
