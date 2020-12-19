# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 10:15:12 2017

@author: jia2015
"""

import os
from xml.etree.ElementTree import parse,tostring

#path='/home/tom/darkflow/train/dataset_broken/images/train/xml/'
path='/home/tom/darkflow/train/dataset_broken/images/test_convert/xml/'
files = os.listdir(path)
i=1
for xmlfile in files:
    
    file_name,file_extend=os.path.splitext(xmlfile)
    
    doc = parse(path+xmlfile)
    
    elem_=doc.findall('folder')[0]
    elem_.text='train'
    
    elem=doc.findall('filename')[0]
    elem.text=file_name+'.jpg'
    
    elem1=doc.findall('path')[0]
    elem1.text="/home/test/darkflow/train/"+file_name+'.jpg'
    
    #elem.text= "/home/test/darkflow/VOCdevkit/VOC2007/JPEGImages/"+xmlfile.replace('.xml','.jpg')
    #elem=doc.findall('folder')[0]
    #elem.text= 'train'
    doc.write(path+xmlfile) 
    i=i+1
