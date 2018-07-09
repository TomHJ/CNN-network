import os
import glob
import shutil

path_tmp="D:\\yolo_experiment\\test_180706\\data\\training_set_test\\"
path_train="D:\\yolo_experiment\\test_180706\\data\\training_set_test\\NG\\"
path_OK="D:\\yolo_experiment\\test_180706\\data\\training_set_test\\OK\\"

files_txt_train=glob.glob(path_train+"*.txt")

for file in files_txt_train:
    statinfo=os.stat(file)
    if statinfo.st_size==0:
        file_txt=file.split(sep="NG\\")[1]
        file_base=file_txt.split(sep=".")[0]
        shutil.move(file,path_OK+file_txt);
        shutil.move(path_train+file_base+".bmp", path_OK + file_base+".bmp");

