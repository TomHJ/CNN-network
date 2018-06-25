#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 11:35:57 2018

@author: test
"""

import os
import cv2
import numpy as np
#from numpy import *

img_dir='/home/test/segmentation/ICNet-tensorflow/dataset/dataset2/rgb/'
img_list=os.listdir(img_dir)
#img_size=224

# method 1
sum_=0
count=0
for img_name in img_list:
    img_path=os.path.join(img_dir,img_name)
    img=cv2.imread(img_path)
    sum_=sum_+np.sum(img,axis=(0,1))/(img.shape[0]*img.shape[1])
    count=count+1
print(sum_/count)


# method 2
sum_r=0
sum_g=0
sum_b=0
count=0

for img_name in img_list:
    img_path=os.path.join(img_dir,img_name)
    img=cv2.imread(img_path)
    sum_r=sum_r+img[:,:,0].mean()
    sum_g=sum_g+img[:,:,1].mean()
    sum_b=sum_b+img[:,:,2].mean()
    count=count+1

sum_r=sum_r/count
sum_g=sum_g/count
sum_b=sum_b/count
img_mean=[sum_r,sum_g,sum_b]
print(img_mean)
