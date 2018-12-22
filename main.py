import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from keras.utils.np_utils import to_categorical
import tensorflow as tf
from load import load

x_train, y_train, x_test, y_test, classes = load()
y_train = to_categorical(y_train, num_classes=6)
y_test = to_categorical(y_test, num_classes=6)
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(name='first'),
    tf.keras.layers.Dense(512, activation=tf.nn.relu, name='second'),

    tf.keras.layers.Dense(256, activation=tf.nn.relu, name='third'),
    tf.keras.layers.Dense(256, activation=tf.nn.relu, name='fourth'),
    tf.keras.layers.Dense(6, activation=tf.nn.softmax, name='fifth')
])

model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, batch_size=50)
result = model.evaluate(x_test, y_test)
print(result)
