import tensorflow as tf
import numpy as np
import time
import cv2
import pickle
import sys



with open('label_class.pickle', 'rb') as f:
    label_class = pickle.load(f)

# with open('test.pickle', 'rb') as f:
#     test = pickle.load(f)
#
# new_model = tf.keras.models.load_model('test9.model')

def recognition(img_path):
    # img_path = '/home/ivliev/test_tensorflow/Machine_Learning/images/3021.png'

    img = cv2.imread(img_path)
    img = cv2.resize(img,(int(50),int(50)))

    img = img/255.0
    data = img
    test_array = []
    test_array.append(data)
    test_array = np.array(test_array)

    new_model = tf.keras.models.load_model('/home/ivliev/Bot_ML/test9.model')
    # new_model = tf.keras.models.load_model('test.model')

    # x1 = time.time()
    predictions = new_model.predict(test_array)
    # x2 = time.time()

    print(np.argmax(predictions[0]))
    print(predictions)
    return np.argmax(predictions[0])

# x = recognition('/home/ivliev/test_tensorflow/Machine_Learning/images/3021.png')

# plt.imshow(data,cmap=plt.cm.binary)
# plt.show()
