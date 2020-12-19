import os
from shutil import copyfile

path='D:/total_180301/'
path1='D:/total_180301/xml/'
path2='D:/total_180301/images/'
files_A= os.listdir(path)
files_B = os.listdir(path1)

for file_A in files_A:
    for file_B in files_B:
        if file_A.split(".")[0]==file_B.split(".")[0]:
            #copyfile(path1+file_B,path2+file_B)
            copyfile(path+file_A,path2+file_A)
            

