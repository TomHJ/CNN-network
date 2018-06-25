# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 10:15:12 2017

@author: jia2015
"""

import os

path = '/home/test/object_detection/AlexeyAB_darknet/darknet/experiment_180622/data/train/'
path1 = '/home/test/object_detection/AlexeyAB_darknet/darknet/experiment_180622/data/img/'

files_bmp = os.listdir(path)

with open("/home/test/object_detection/AlexeyAB_darknet/darknet/experiment_180622/data/train_2.txt","w") as f:
    for file in files_bmp:
        file_without_extension=file.split('.')[0]
        f.write(path1+file_without_extension+".bmp"+"\n")
        


