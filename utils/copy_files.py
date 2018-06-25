import os
from shutil import copyfile


path="/home/test/object_detection/AlexeyAB_darknet/darknet/experiment_180625/data/test.txt"

path_dst="/home/test/object_detection/AlexeyAB_darknet/darknet/experiment_180625/data/test_img/"

with open(path,'r') as f:
    lines=f.readlines()
    for line in lines:
        copyfile(line.strip(), path_dst+line.strip().split(sep=r"/img/")[1])



            

