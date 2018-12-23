# Neural Network Results
|**Architecture** | **epochs** | **batch-size** | **optimizer** | **Train-acc** | **Test-acc**|**Loss-func**|ملاحظات|
|---|---|---|---|---|---|---|---|
|6912->tanh(6912)->tanh(3456)->tanh(864)->tanh(432)->softmax(6)|20|50|sgd|0.72|0.58|categorical||
|6912->tanh(5000)->tanh(5000)->tanh(5000)->tanh(5000)->softmax(6)|20|50|adam|0.15|0.18|categorical||
|6912->tanh(500)->tanh(500)->tanh(500)->tanh(500)->softmax(6)|20|50|adam|0.23|0.22|categorical||
|6912->relu(500)->relu(500)->relu(500)->relu(500)->softmax(6)|20|50|adam|0.78|0.56|categorical||
|6912->relu(500)->relu(500)->relu(500)->relu(500)->softmax(6)|70|50|adam|0.99|0.63|categorical||
|6912->relu(1000)->relu(1000)->relu(1000)->relu(1000)->softmax(6)|50|40|adam|0.91|0.61|categorical||
|6912->relu(1000)->relu(1000)->relu(1000)->relu(1000)->softmax(6)|50|40|adam|0.94|0.88|binary||
|6912->relu(1000)->relu(1000)->relu(1000)->relu(1000)->softmax(6)|50|40|rmsprop|0.25|0.22|categorical|loss doesn't change|
|6912->relu(1000)->tanh(1000)->relu(1000)->tanh(1000)->softmax(6)|50|40|rmsprop|0.25|0.22|categorical|loss doesn't change|
|6912->relu(1000)->tanh(1000)->relu(1000)->tanh(1000)->softmax(6)|30|40|Adam|0.31|0.28|categorical||
|6912->relu(1000)->tanh(1000)->relu(1000)->tanh(1000)->softmax(6)|30|10|Adam|0.21|0.13|categorical||
|6912->relu(1000)->relu(1000)->relu(1000)->relu(1000)->softmax(6)|30|100|Adam|0.79|0.57|categorical||
|6912->relu(1000)->relu(1000)->relu(1000)->relu(1000)->softmax(6)|100|100|Adam|1|0.62|categorical|over fitting|
|6912->relu(1000)->relu(1000)->relu(1000)->relu(1000)->softmax(6)|50|100|Adam|0.92|0.62|categorical||
|6912->relu(1000)->relu(1000)->relu(1000)->relu(1000)->softmax(6)|40|100|Adam|0.85|0.62|categorical||
|6912->relu(1000)->relu(1000)->relu(1000)->relu(1000)->softmax(6)|30|100|Adam|0.78|0.55|categorical||
|6912->relu(500)->relu(500)->softmax(6)|70|50|Adam|0.98|0.62|categorical||

# Conclusion
>After trying a lot we can conclude that the best test accuracy we can get is
0.62 using *Keras Categorical loss*. Although *Keras Binary Cross entropy* produce better test result. 
After some investigation we compared the 2 functions' implementations:


```python
def binary_accuracy(y_true, y_pred):
    return K.mean(K.equal(y_true, K.round(y_pred)), axis=-1)
def categorical_accuracy(y_true, y_pred):
     return K.cast(K.equal(K.argmax(y_true, axis=-1),K.argmax(y_pred, axis=-1)),K.floatx())
# The most suitable one for multi-classes and hot encodings is the categorical accuracy.
```

>The activation Relu showed great converge through global minimum in a small number of iteration but sometimes it stuck. 
I think the reason is the negative numbers that change to zero and thus the network freezes. Softmax is crucial in the output layer.

>Optimizer Adam is better than sgd(stochastic gradient descent) and rmsprop as it combines sgd and momentum

>Small batches slow down the overall speed of iterations.

>We examined some of the test data that are wrongly predicted.













     