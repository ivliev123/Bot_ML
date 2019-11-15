import tensorflow as tf
import numpy as np
import time
import cv2
import pickle
import sys



# with open('/home/ivliev/Bot_ML/label_class.pickle', 'rb') as f:
#     label_class = pickle.load(f)


# new_model = tf.keras.models.load_model('/home/ivliev/Bot_ML/test11.model')

def recognition(img_path):

    img = cv2.imread(img_path)
    img = cv2.resize(img,(int(50),int(50)))

    img = img/255.0
    data = img
    test_array = []
    test_array.append(data)
    test_array = np.array(test_array)

    new_model = tf.keras.models.load_model('/home/ivliev/Bot_ML/test11.model')

    # x1 = time.time()
    predictions = new_model.predict(test_array)
    # x2 = time.time()

    # print(predictions)
    # return np.argmax(predictions[0])
    return predictions

def predictions_out(img_path, label_class):
    predictions = recognition(img_path)
    n = 3
    max_3_predict_index = np.argsort(predictions[0])[-n:]
    max_3_predict = predictions[0][max_3_predict_index]

    label_class = np.array(label_class)
    label = label_class[:,0]
    label = list(label)

    array_out = []
    for i in range(max_3_predict_index.size):
        index = label.index(str(max_3_predict_index[i]))
        class_ = label_class[index][1]
        if(max_3_predict[i] > 0.005):
            array_out.append([class_ , max_3_predict[i]*100.00])

    array_out = sorted(array_out, key=lambda x : x[1], reverse = True)

    return array_out
