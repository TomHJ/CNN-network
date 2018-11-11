# marked web which i am interested in and want to study from
http://mirai-tec.hatenablog.com/


# custome data process pipline

step1: generator of image path and labels

import tensorflow as tf
import cv2
import os
from random import shuffle
import numpy as np

path_train_imageset='/home/tom/workspace/dataset/classification/'

# load imageset
addrs=[]
labels=[]
directories=os.listdir(path_train_imageset)
for directory in directories:
    for file in os.listdir(path_train_imageset+directory):
        if '.bmp' in file:
            addrs.append(path_train_imageset+directory+'/'+file)
            labels.append(directory)

c=list(zip(addrs,labels))
shuffle(c)
addrs,labels=zip(*c)

# load image
def load_image(addr):
    img=cv2.imread(addr)
    img=cv2.resize(img,(448,448))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return np.array(img)

num_epoches=100
size=len(addrs)
batch_size=32
batch_per_epoch=int(size/batch_size)
for i in range(num_epoches):
    shuffle_idx=perm(np.arange(size))
    for b in range(batch_per_epoch):
        x_batch=list()
        y_batch=list()

        for j in range(b*batch_size,(b+1)*batch_size):
            img=load_image(addrs[j])
            label=np.array(labels[j])



