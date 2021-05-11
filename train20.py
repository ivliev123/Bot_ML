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

with open('label_class.pickle', 'rb') as f:
    label_class = pickle.load(f)

data = np.array(data)
# print(data.shape)

label_class = np.array(label_class)
# print(label_class.shape[0])


x_train = []
y_train = []

for i in  range(data.shape[0]):
    x_train.append(data[i][0])
    y_train.append(data[i][1])

y_train = np.array(y_train)
y_train.astype(np.uint8)

x_train = np.array(x_train)


# print(len(x_train))
# print(len(y_train))


# input_shape = (50, 50, 3)
input_shape=x_train.shape[1:]
# print(input_shape)

x_train = tf.keras.utils.normalize(x_train, axis = 1)

model = Sequential()

model.add(Conv2D(128, kernel_size=(5,5), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(256, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(256, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

# model.add(Dense(1024, activation=tf.nn.relu))
# model.add(Dense(512, activation=tf.nn.relu))
model.add(Dense(128, activation=tf.nn.relu))
model.add(Dropout(0.2))
# model.add(Dense(label_class.shape[0],activation = tf.nn.softmax))
model.add(Dense(4,activation = tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Создаем коллбек сохраняющий веса модели
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1, period=10)

model.save_weights(checkpoint_path.format(epoch=0))

model.summary()
# model.fit(x_train, y_train, batch_size=500, epochs=100, callbacks=[cp_callback])
model.fit(x_train, y_train, batch_size=500, epochs=2, callbacks=[cp_callback])



model.save('test12.model')
