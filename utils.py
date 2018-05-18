# -*- coding: utf-8 -*-
"""
@author: admin
"""

### Collection of functions


import glob
import urllib.request
import cv2
import numpy as np
import pickle
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

#------------------- Remove files ---------------------------#

def remove_extra_files(Dir_to_remove = Dir_to_remove):
    Dir_to_remove = os.chdir(Dir_to_remove)
    types = ('*.ppm', '*.txt')
    files_to_remove = []
    for files in types:
        files_to_remove.extend(glob.glob(files))
     
    # print("Files to remove: ", files_to_remove)    
    for file2 in files_to_remove:
         os.remove(file2)


#------------------- load image from folder  ---------------------------#

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith('ppm'):
            img = cv2.imread(os.path.join(folder, filename))
           # img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            img_resize=cv2.resize(img,(32,32))
            if img_resize is not None:
                images.append(img_resize)   
    return images 

#------------------- generate fuatures and targets  ---------------------------#

dir_folders = os.listdir("images/train/FullIJCNN2013/") # get all files' and folders' names in the current directory


def generate_features_targets(dir_folders) :
    
        folders = os.listdir(dir_folders)
    
        features = []
        target = []
        
        for folder in folders:
            images = load_images_from_folder( dir_folders + folder)
            if images is not None:
              features.extend(images)  
              nu = np.repeat(folder, len(images))
              target.extend(nu)
        
        features1 = np.asarray(features)
        
        target1 = np.asarray(target)
        
        data = {'features': features1, 'target': target1}

        return data


#------------------- split data set ---------------------------#

def split_store (feature, target ):
    #taking random data from the dataset
    x,y=shuffle(feature,target,random_state=2)
    
    #spliting the data into test and train
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)
    
    plt.imsave('filename.ppm', np.array(data).reshape(50,50), cmap=cm.gray)
    
    # Store data (serialize)
    with open('Features.p', 'wb') as handle:
        pickle.dump(features1, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    # Store data (serialize)
    with open('Target.p', 'wb') as handle:
        pickle.dump(target1, handle, protocol=pickle.HIGHEST_PROTOCOL)
