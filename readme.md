# Detectioner
##### A FACE DETECTION PROJECT

1. Collecting data set: 250 pics of each project member cropped to his face only with size 48 * 48 pixel. 
It will be placed in the photos directory with nearly more than 1500 photo.

2. Build Face detection model using only neural network with Keras. **(noconv.ipynb)** 

3. Build Face detection model using neural network and convolution. **(conv.ipynb)**

After building both models the process of choosing hyperparameters like 
activation functions, network architecture, epochs and many other parameters remains.

In the rep there are 2 files (results.md & conv-results.md). They contain the 
result of choosing different parameters and how they are reflected on the 
training and the test accuracy.

>Environment Setup: I have used miniconda3 to install all needed packages like tensorflow