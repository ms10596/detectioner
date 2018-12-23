# Convolution and neural network result
|Architecture|epochs|batch-size|optimizer|Train-acc|Test-acc|Loss-func|ملاحظات
|---|---|---|---|---|---|---|---|
|relu(conv2d(3))->maxpooling->relu(500)->relu(500)->softmax(6)|20|50|1|0.69|
|relu(conv2d(3))->maxpooling->relu(500)->relu(500)->softmax(6)|10|50|0.99|0.59|
|relu(conv2d(3))->maxpooling->relu(500)->relu(500)->softmax(6)|100|50|1|0.62|
|conv2d(3)->batchnormalization->maxpooling(2)->relu(500)->relu(500)->softmax(6)|20|50|1|0.7|
|conv2d(5)->batchnormalization->maxpooling(2)->relu(500)->relu(500)->softmax(6)|20|50|1|0.73|
|conv2d(5)->batchnormalization->maxpooling(2)->relu(500)->relu(500)->softmax(6)|10|50|0.996|0.68|
|conv2d(5)->batchnormalization->maxpooling(2)->relu(500)->softmax(6)|10|50|0.99|0.68|
|conv2d(5)->batchnormalization->maxpooling(2)->relu(500)->softmax(6)|20|50|1|0.68|
|conv2d(5)->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|20|50|1|0.71|
|conv2d(5)->batchnormalization->maxpooling(5)->conv2d(5)->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|20|50|0.57|0.3|
|conv2d(5)->batchnormalization->maxpooling(5)->conv2d(5)->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|40|50|0.64|0.59|
|relu(conv2d(5))->batchnormalization->maxpooling(5)->relu(conv2d(5))->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|40|50|0.54|0.38|
|relu(conv2d(5, channels=10))->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|20|50|1|0.73|same padding
|relu(conv2d(5, channels=10))->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|40|50|1|0.78|same padding
|relu(conv2d(5, channels=10))->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|40|50|1|0.78|valid padding
|relu(conv2d(5, channels=10))->batchnormalization->maxpooling(3)->relu(500)->softmax(6)|40|50|1|0.75|valid padding
|relu(conv2d(5, channels=20))->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|50|50|1|0.81|valid padding
|tanh(conv2d(5, channels=20))->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|20|50|0.9|0.81|valid padding
|relu(conv2d(5, channels=30))->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|90|50|0.9|0.84|valid padding
|relu(conv2d(5, channels=40))->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|100|50|1|0.82|
|relu(conv2d(3, channels=32))->batchnormalization->maxpooling(2)->relu(conv2d(3, channels=32))->batchnormalization->maxpooling(2)->relu(500)->softmax(6)|50|50|1|0.81|
|relu(conv2d(3, channels=32))->batchnormalization->maxpooling(2)->relu(conv2d(3, channels=12))->batchnormalization->maxpooling(2)->relu(500)->softmax(6)|150|50|1|0.80|
|relu(conv2d(3, channels=32))->batchnormalization->maxpooling(2)->relu(conv2d(3, channels=12))->batchnormalization->maxpooling(2)->relu(100)->softmax(6)||50|1|0.8|
|relu(conv2d(3, channels=100))->batchnormalization->maxpooling(2)->relu(100)->softmax(6)|100|50|1|0.79|
|relu(conv2d(3, channels=30))->batchnormalization->maxpooling(5)->relu(500)->softmax(6)|50|50|1|0.85|


# Conclusion
>Convolution has improved accuracy from 0.62 to 0.82






