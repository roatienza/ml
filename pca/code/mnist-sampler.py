'''
Demonstrates how to sample and plot MNIST digits
using Keras API
https://github.com/PacktPublishing/Advanced-Deep-Learning-with-Keras
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# sample 1 mnist digit from train dataset
indexes = np.random.randint(0, x_train.shape[0], size=1)
images = x_train[indexes]
labels = y_train[indexes]

for i in range(len(indexes)):
    image = images[i]
    label = labels[i]
    plt.imshow(image, cmap='gray')
    plt.axis('off')

plt.savefig('{0}.png'.format(label))
plt.show()
plt.close('all')
