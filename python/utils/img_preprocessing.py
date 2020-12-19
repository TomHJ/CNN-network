#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:17:56 2018

@author: test
"""

import cv2
import os
import numpy as np

img_path='/home/test/workspace/study/preprocessing/dataset/img/'

files=os.listdir(img_path)

X=[]
for file in files:
    img=cv2.imread(img_path+file)
    #X.append(img)
    X.append(np.expand_dims(img,0))

X_=np.concatenate(X, 0)
#X_=np.array(X)   # X_ is numpy.ndarray (600, 750, 1000, 3)
                 # 600 is number of sample

X_flatten=X_.reshape(X_.shape[0],-1).T   # X_flatten is numpy.ndarray (2250000, 600)
pass                                        # 600 is number of sample