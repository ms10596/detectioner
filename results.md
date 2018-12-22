# Neural Network Results
|**Architecture** | **epochs** | **batch-size** | **optimizer** | **Train-acc** | **Test-acc**|**Loss-func**|
|---|---|---|---|---|---|---|
|6912->tanh(6912)->tanh(3456)->tanh(864)->tanh(432)->softmax(6)|20|50|sgd|0.72|0.58|categorical|
|6912->tanh(5000)->tanh(5000)->tanh(5000)->tanh(5000)->softmax(6)|20|50|adam|0.15|0.18|categorical|
|6912->tanh(500)->tanh(500)->tanh(500)->tanh(500)->softmax(6)|20|50|adam|0.23|0.22|categorical|
|6912->relu(500)->relu(500)->relu(500)->relu(500)->softmax(6)|20|50|adam|0.78|0.56|categorical|
|6912->relu(500)->relu(500)->relu(500)->relu(500)->softmax(6)|70|50|adam|0.99|0.63|categorical|
|6912->relu(1000)->relu(1000)->relu(1000)->relu(1000)->softmax(6)|50|40|adam|0.91|0.61|categorical
|6912->relu(1000)->relu(1000)->relu(1000)->relu(1000)->softmax(6)|50|40|adam|0.94|0.88|binary|



     