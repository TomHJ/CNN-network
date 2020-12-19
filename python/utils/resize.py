# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 10:15:12 2017

@author: jia2015
"""

import os
import cv2

path='/home/test/workspace/ICNet-tensorflow/dataset/dataset2/val/rgb/'
path1='/home/test/workspace/ICNet-tensorflow/dataset/dataset2/val/rgb_new_size/'
files = os.listdir(path)
#i = 1

for file in files:
    img=cv2.imread(path+file,cv2.IMREAD_UNCHANGED)        
    if img is not None:
        #w,h,c=img.shape
        #img1=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
        img2=cv2.resize(img,(1024,768))        
        cv2.imwrite(path1+file,img2)        
        #i +=1
