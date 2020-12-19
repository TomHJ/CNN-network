#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:57:50 2018

@author: test
"""

import os

path="/home/test/object_detection/AlexeyAB_darknet/darknet/experiment_180615/process_txt/"
#path="/home/test/object_detection/AlexeyAB_darknet/darknet/experiment_180615/tmp/"
files=os.listdir(path)

for file in files:
    data=''
    with open(path+file,mode='r+') as f:
        for line in f.readlines():
            if line[0]=='0':
                data +='2'+line[1:]
            elif line[0]=='2':
                data +='0'+line[1:]

    with open(path+file,'r+') as f:
        f.writelines(data)