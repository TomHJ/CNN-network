# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 10:15:12 2017

@author: jia2015
"""

import os

path = '/home/tom/util/image/train/'

files = os.listdir(path)

for file in files:
    os.rename(path+file,path+"A"+file)