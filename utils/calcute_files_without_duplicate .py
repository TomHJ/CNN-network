'''

# 统计2016/2520产品系列各子目录的图片数量；同时看下有没有同名的图片
2018.10.30

'''

import os


path_root="/media/tom/Seagate Backup Plus Drive/old/customer_dataset/classification_dataset/2016/"


directories=os.listdir(path_root)

files_all=[]

i=0

try:
    for directory in directories:
        for file in os.listdir(path_root+directory):
            if ".bmp" in file:
                if file not in files_all:
                    files_all.append(file)
                else:
                    i +=1
                    with open("log.txt","a") as f:
                        f.write(path_root+directory+"/"+file)

except Exception as e:
    print(e)


print(len(files_all))
print("{} files duplicated".format(str(i)))