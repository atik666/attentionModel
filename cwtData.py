from IPython import get_ipython
get_ipython().magic('reset -sf')
import numpy as np
import cv2
import os

# All the categories you want your neural network to detect
CATEGORIES = ["Norm","Ball0.007","Ball0.014","Ball0.021",
              "Inner0.007","Inner0.014","Inner0.021",
              "Outer0.007","Outer0.014","Outer0.021"]

# Checking or all images in the data folder
def import_data(DATADIR):
    training_data = []
    for category in CATEGORIES :
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
            os.path.join(DATADIR, category)
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
            img_array = np.expand_dims(img_array, axis=0)
            training_data.append([img_array, class_num])

    X = [] #features
    y = [] #labels

    for features, label in training_data:
    	X.append(features)
    	y.append(label)

    X = np.array(X)

    x_train = np.squeeze(X).astype('float32')
    x_train /= 255
    y_train = np.array(y).astype('float32')

    return x_train, y_train

path  = 'D:/OneDrive - ump.edu.my/Atik_Home/Writing/Encoder/CWT/'
X, y = import_data(path)
