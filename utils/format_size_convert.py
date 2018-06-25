# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 10:15:12 2017

@author: jia2015
"""

import os
import cv2


path='/home/test/Public/dataset/20180417/process_data/images/'

path_1='/home/test/Public/dataset/20180417/process_data/images_1/'


files = os.listdir(path)
i = 1

for file in files:
    img=cv2.imread(path+file,cv2.IMREAD_UNCHANGED)        
    if img is not None:
        img1=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
        img2=cv2.resize(img1,(1000,750))        
        cv2.imwrite(path_1+file.split(".")[0]+'.jpg',img2)
        #cv2.imwrite(path+'yushi_'+str(i)+'.jpg',img)
        i=i+1
        
        
        