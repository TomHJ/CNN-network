import os
import glob
from shutil import copyfile

path_train="D:\\yolo_experiment\\test_180710\\data\\img\\"
#path_test="C:\\Users\\jia2015\\Desktop\\utility\\Yolo_mark\\x64\\Release\\data\\0624\\test\\"
#path_add="C:\\Users\\jia2015\\Desktop\\utility\\Yolo_mark\\x64\\Release\\data\\0624\\test_add\\"

#path_tmp="C:\\Users\\jia2015\\Desktop\\utility\\Yolo_mark\\x64\\Release\\data\\0624\\temp\\"

#files_train=os.listdir(path_train)
files_txt_train=glob.glob(path_train+"*.txt")
#files_test=os.listdir(path_test)

#files_temp=os.listdir(path_tmp)

# for file in files_temp:
#     os.remove(path_test + file)


count=dict()
count['CiTiLouTong'] =0; count['CiTiQueSun'] =0
count['CiTiLieWen'] =0; count['DuanZiJunLie'] =0
count['DuanZiDuanQueGuoChang'] =0; count['DuanZiYaShang'] =0
count['DuanZiQiaoQi'] =0; count['DuanZiMaoBian'] =0
count['DuanZiZangWu'] =0; count['CiTiZangWu'] =0
count['DuanZiLouTong'] =0

for file in files_txt_train:
    with open(file,'r') as f:
        lines=f.readlines()
        for line in lines:
            if line[0]==str('0'):
                count['CiTiLouTong'] +=1
                #copyfile(path_test+file, path_add + file)
                #os.remove(path1 + file)
            elif line[0]==str('1') and line[1] != str('0'):
                count['CiTiQueSun'] +=1
            elif line[0]==str('2'):
                count['CiTiLieWen'] +=1
            elif line[0]==str('3'):
                count['DuanZiJunLie'] +=1
            elif line[0]==str('4'):
                count['DuanZiDuanQueGuoChang'] +=1
            elif line[0]==str('5'):
                count['DuanZiYaShang'] +=1
            elif line[0]==str('6'):
                count['DuanZiQiaoQi'] +=1
            elif line[0]==str('7'):
                count['DuanZiMaoBian'] +=1
            elif line[0]==str('8'):
                count['DuanZiZangWu'] +=1
            elif line[0]==str('9'):
                count['CiTiZangWu'] +=1
            elif line[0]==str('1') and line[1]==str('0'):
                count['DuanZiLouTong'] +=1

print(count)
