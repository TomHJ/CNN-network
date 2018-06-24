import os
from shutil import copyfile

path_train="C:\\Users\\jia2015\\Desktop\\utility\\Yolo_mark\\x64\\Release\\data\\0624\\train\\"
path_test="C:\\Users\\jia2015\\Desktop\\utility\\Yolo_mark\\x64\\Release\\data\\0624\\test\\"
path_add="C:\\Users\\jia2015\\Desktop\\utility\\Yolo_mark\\x64\\Release\\data\\0624\\test_add\\"

path_tmp="C:\\Users\\jia2015\\Desktop\\utility\\Yolo_mark\\x64\\Release\\data\\0624\\temp\\"

files_train=os.listdir(path_train)
files_test=os.listdir(path_test)

files_temp=os.listdir(path_tmp)

# for file in files_temp:
#     os.remove(path_test + file)


count=dict();count['loutong'] =0; count['bengque'] =0

for file in files_train:
    with open(path_train+file,'r') as f:
        lines=f.readlines()
        for line in lines:
            if line[0]==str('0'):
                count['loutong'] +=1
                #copyfile(path_test+file, path_add + file)
                #os.remove(path1 + file)
            elif line[0]==str('1'):
                count['bengque'] +=1

print(count)
