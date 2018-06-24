import os

path_train="C:\\Users\\jia2015\\Desktop\\utility\\Yolo_mark\\x64\\Release\\data\\0624\\train\\"
path_test="C:\\Users\\jia2015\\Desktop\\utility\\Yolo_mark\\x64\\Release\\data\\0624\\test\\"

files_train=os.listdir(path_train)
files_test=os.listdir(path_test)

with open("C:\\Users\\jia2015\\Desktop\\utility\\Yolo_mark\\x64\\Release\\data\\0624\\train.txt",'a') as f:
    for file in files_train:
        f.write(path_test+file.split('.')[0]+'.bmp'+'\n')

