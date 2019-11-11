import csv
import cv2
import copy
import pickle
import numpy as np

# прочитать файл CSV индексом найти номер иполучить название класса


def data_to_train_test(file_obj):

    # row_count = sum(1 for row in file_obj)
    # print(row_count)
    reader = csv.DictReader(file_obj, delimiter=',')

    max_col_of_class = 150
    col_of_each_class = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    pickle_array_train = []
    pickle_array_test = []
    label_class = []

    labels = []
    for l in range(25):
        labels.append(str(l))
    # print(labels)

    for line in reader:
        # print(line["boxid"]),
        # print(line["label"])
        # print(line["class_"])
        boxid = line["boxid"]
        label = line["label"]
        class_ = line["class_"]

        for ll in labels:
            if(ll == label):
                label_class.append([label,class_])
                labels.pop(labels.index(label))

        label = int(label)
        col_of_each_class[label] +=1

        image_name = 'Machine_Learning/images/' + str(boxid) + '.png'
        img = cv2.imread(image_name)
        img = cv2.resize(img, (100,100))
        img_array = np.array(img)

        if(col_of_each_class[label] < max_col_of_class*0.95):
            pickle_array_train.append([img_array,label])
        else:
            pickle_array_test.append([img_array,label])

    # print(label_class)
    # print(len(label_class))
    return pickle_array_train, pickle_array_test, label_class

def write_to_picle(array, name):
    with open(name+'.pickle', 'wb') as f:
        pickle.dump(array, f)

if __name__ == "__main__":
    csv_path = "Machine_Learning/images_labelling.csv"
    with open(csv_path, "r") as f_obj:
        pickle_array_train, pickle_array_test, label_class = data_to_train_test(f_obj)
    write_to_picle(pickle_array_train,'train')
    write_to_picle(pickle_array_test,'test')
    write_to_picle(label_class,'label_class')
