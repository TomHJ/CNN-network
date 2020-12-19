 
import os
from os import listdir, getcwd
from os.path import join
if __name__ == '__main__':
    source_folder_jpg='/home/tom/darkflow/train/dataset_broken/images/test_convert/jpg/'
    source_folder_xml='/home/tom/darkflow/train/dataset_broken/images/test_convert/xml/' 
    #train='/home/tom/darkflow/train/dataset_broken/images/train.txt' 
    #train_xml='/home/tom/darkflow/train/dataset_broken/images/train_xml.txt'
    train='/home/tom/darkflow/train/dataset_broken/images/test.txt' 
    train_xml='/home/tom/darkflow/train/dataset_broken/images/test_xml.txt'   
    file_list=os.listdir(source_folder_xml)        
    train=open(train,'a')  
    train_xml=open(train_xml,'a')                 
    i=901
    for file in file_list:                 
        
        file_name,file_extend=os.path.splitext(file)
        
        old_file_name_xml=file_name+'.xml'
        old_file_name_jpg=file_name+'.jpg'
        
        new_file_name_xml=str(format(i,'05d'))+'.xml'
        new_file_name_jpg=str(format(i,'05d'))+'.jpg'
        
        old_file_xml=os.path.join(source_folder_xml,old_file_name_xml)
        new_file_xml=os.path.join(source_folder_xml,new_file_name_xml)
        
        old_file_jpg=os.path.join(source_folder_jpg,old_file_name_jpg)
        new_file_jpg=os.path.join(source_folder_jpg,new_file_name_jpg)
        
        os.rename(old_file_xml,new_file_xml)
        os.rename(old_file_jpg,new_file_jpg)

          
        train_xml.write(old_file_name_xml+" --> "+new_file_name_xml+'\n')
        train.write(old_file_name_jpg+" --> "+new_file_name_jpg+'\n')
        
        i=i+1

    train.close()
    train_xml.close()
