# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 09:46:58 2018

IMPORTANT :
    1. This project is for a specific type of folder arrangement of dataset
    2. Please intall : {1.Theano  ,  2.Tensorflow  ,  3.Keras}  before executing it.
    3. Replace the folder names according to your own requirements
    
NOTE : Dataset is empty but structured ; use your own
@author: Udit
"""
# Convolutional Neural Network


# Importing the required libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


"""
Building a CNN requires the following steps :
    1. Convolution
    2. Pooling
    3. Flattening
    4. Full connection
    5. Compiling
"""