# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 10:15:12 2017

@author: jia2015
"""

import os
import cv2
#path = 'D:/caffe_python/caffe-master/vgg_face/sample2/train/image/meixi'
#path = 'D:/1'
#path = 'D:/people/bingbing/god'
#path='D:/OpenCV_Project/opencv-3.3.1/build/install/x64/vc14/lib'
#path = 'D:/Projects/object_recognition/test'
#path = 'C:/Users/jia2015/Desktop/vgg16_face_demo/image/wjk'
path = '/home/tom/util/image/test/'

files = os.listdir(path)
i = 1

for file in files:
    img=cv2.imread(path+file,cv2.IMREAD_UNCHANGED)        
    if img is not None:
        #img1=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
        #img2=cv2.resize(img1,(1000,750))        
        #cv2.imwrite(path+file.split(".")[0]+'.jpg',img2)
        cv2.imwrite(path+'A'+file,img)
        i=i+1