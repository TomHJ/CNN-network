# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 10:15:12 2017

@author: jia2015
"""

from PIL import Image
filename="C:/Users/deepl/Desktop/utility/s1NG_2016_3391_1609_s1_NG_6.bmp"
try:
    im=Image.open(filename)
    # do stuff
except IOError:
    with open("train.txt", 'a') as f:
        f.write(filename + '\n')