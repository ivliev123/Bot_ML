import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D


import numpy as np
import pickle
import os

with open('train.pickle', 'rb') as f:
    data = pickle.load(f)

with open('test.pickle', 'rb') as f:
    test = pickle.load(f)

for i in range(len(test)):
    test_images = test[i][0]
    test_labels = test[i][1]

test_images = np.array(test_images)
test_images = test_images/255.0
test_labels = np.array(test_labels)
test_labels.astype(np.uint8)


data = np.array(data)
print(data.shape)


x_train = []
y_train = []

for i in  range(data.shape[0]):
    x_train.append(data[i][0])
    y_train.append(data[i][1])

y_train = np.array(y_train)
y_train.astype(np.uint8)


x_train = np.array(x_train)
input_shape=x_train.shape[1:]
print(input_shape)
# x_train = x_train.reshape( 50, 50, 3)
#
# input_shape=x_train.shape[1:]
# print(input_shape)

checkpoint_dir = "/home/ivliev/test_tensorflow/training_2"
latest = tf.train.latest_checkpoint(checkpoint_dir)
print(latest)

x_train = tf.keras.utils.normalize(x_train, axis = 1)


model = Sequential()

model.add(Conv2D(128, kernel_size=(7,7), input_shape=(input_shape)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(256, kernel_size=(5,5), input_shape=(input_shape)))
model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Conv2D(128, kernel_size=(3,3), input_shape=input_shape))
# model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(1024, activation=tf.nn.relu))
model.add(Dense(512, activation=tf.nn.relu))
model.add(Dense(256, activation=tf.nn.relu))
model.add(Dropout(0.2))
model.add(Dense(len(y_train),activation = tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


model.load_weights(latest)
# loss, acc = model.evaluate(test_images,  test_labels, verbose=1)
# print("Restored model, accuracy: {:5.2f}%".format(100*acc))
model.save('test11.model')
