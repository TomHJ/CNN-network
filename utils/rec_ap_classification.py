import numpy as np

file_name='/home/test/object_detection/darknet/results/comp4_det_test_zhanjiao.txt'
imgs=list()
with open(file_name, 'r') as f:
    lines=f.readlines()
    splitlines = [x.strip().split(' ') for x in lines]
for file in splitlines:
    imgs +=[[file[0],file[1]]]

final_dic=dict()
imgs_array=np.array(imgs)
total_num=imgs_array.shape[0]

final_dic[imgs_array[0][0]] = float(imgs_array[0][1])
for i in range(1,total_num):
    if imgs_array[i][0]==imgs_array[i-1][0]:
        if float(imgs_array[i][1])>final_dic[imgs_array[i-1][0]]:
            final_dic[imgs_array[i-1][0]] = float(imgs_array[i][1])
    else:
        final_dic[imgs_array[i][0]] = float(imgs_array[i][1])
object_images=0
no_object_images=0
for key,val in final_dic.items():
    if val>0.6:
        object_images +=1
    else:
        no_object_images +=1
        print(key,val)

print(str(object_images)+"images have objects")
print(str(no_object_images)+"images have not objects")