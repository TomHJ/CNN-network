# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 10:15:12 2017

@author: jia2015
"""

import os

for i in range(1,8):
    path = "C:\\Users\\jia2015\\Desktop\\2520\\M1800105\\20180611_082229AM\\Stage"+str(i)+"Insp_IMG\\OK\\"
    files = os.listdir(path)
    for file in files:
        os.rename(path+file,path+"2520_0105_2229_s"+str(i)+"_OK_"+file)