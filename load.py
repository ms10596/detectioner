import os
import tensorflow as tf
import matplotlib.image as mpimg
import numpy as np


def load_pics():
    pics = np.empty(shape=(1650, 48, 48, 3), dtype=np.float)
    labels = np.empty(shape=(1650, 1), dtype=np.int)
    cnt = 0
    names = ('ashraf', 'joseph', 'magdy', 'ref', 'sayed', 'Shehab')
    for name in names:
        files = os.listdir('photos/' + name)
        for i in files:
            # print(name, i)

            pics[cnt] = mpimg.imread('photos/' + name + '/' + i)
            labels[cnt] = names.index(name)
            cnt += 1

    return pics, labels, names


def load():
    np.random.seed(0)
    all_data, all_labels, classes = load_pics()

    all_data = np.array(all_data)
    all_labels = np.array(all_labels)

    data_length = len(all_data)

    training_portion = 80 * data_length // 100

    shuffled = np.random.permutation(data_length)
    all_data = all_data[shuffled]
    all_labels = all_labels[shuffled]
    # all_labels = tf.one_hot(all_labels, 6)

    # print(all_labels[0])

    training_data = all_data[0:training_portion]
    test_data = all_data[training_portion:]

    training_labels = all_labels[0:training_portion]
    test_labels = all_labels[training_portion:]

    return training_data, training_labels, test_data, test_labels, classes

# x, y, x1, y1 = load()
# print(y[0])
