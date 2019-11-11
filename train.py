import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D


import numpy as np
import pickle

with open('train.pickle', 'rb') as f:
    data = pickle.load(f)

data = np.array(data)
print(data.shape)


x_train = []
y_train = []

for i in  range(data.shape[0]):
    x_train.append(data[i][0])
    y_train.append(data[i][1])

y_train = np.array(y_train)
y_train.astype(np.uint8)

print(len(x_train))
print(len(y_train))





x_train = tf.keras.utils.normalize(x_train, axis = 1)

model =  tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(50, 50, 3)))
model.add(tf.keras.layers.Dense(5000,activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(3000,activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(1000,activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(500,activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(len(y_train),activation = tf.nn.softmax))


model.compile(optimizer = 'adam',
                loss = 'sparse_categorical_crossentropy',
                metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=500, epochs=500)



model.save('test.model')
