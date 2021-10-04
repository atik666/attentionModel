from IPython import get_ipython
get_ipython().magic('reset -sf')
import numpy as np
import os
import cv2

CATEGORIES = ["3Norm","3BF07","3IR07","3OR07"]

# The size of the images that your neural network will use
IMG_SIZE = 64
channel = 3

# Checking or all images in the data folder
def import_data(DATADIR):
    training_data = []
    for category in CATEGORIES :
   		path = os.path.join(DATADIR, category)
   		class_num = CATEGORIES.index(category)
   		for img in os.listdir(path):
   			try :
   				img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
   				#new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
   				training_data.append([img_array, class_num])
   			except:
   				pass

    #random.shuffle(training_data)

    X = [] #features
    y = [] #labels

    for features, label in training_data:
    	X.append(features)
    	y.append(label)

    #X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, channel)
    X = np.array(X)

    x_train = np.squeeze(X).astype('float32')
    x_train /= 255
    y_train = np.array(y).astype('float32')

    return x_train, y_train

Path = "D:/OneDrive - ump.edu.my/Atik_Home/Writing/Encoder/Load data/3"
X, y = import_data(Path)

np.save(Path + "/3Test/3X_test.npy", X)