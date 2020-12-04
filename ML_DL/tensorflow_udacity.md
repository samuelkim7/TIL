## Introduction to Machine Learning
### Basic concept and code structure
- Just give pairs of input and output and let the computer figure out the best algorithm. And this learning process is done by tuning the variables of the equation.
```python
l0 = tf.keras.layers.Dense(units=1, input_shape=[1]) 
model = tf.keras.Sequential([l0])
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
model.predict([100.0])
```
- This example is the general plan for of any machine learning program. You will use the same structure to create and train your neural network, and use it to make predictions.

### The Training process
- The training process (happening in model.fit(...)) is really about tuning the internal variables of the networks to the best possible values, so that they can map the input to the output. This is achieved through an optimization process called Gradient Descent.
  - The model applies its internal math on the input and internal variables to predict an answer.
  - The value of the loss is calculated using a loss function, which we specified with the loss parameter when calling model.compile().
  - Gradient Descent: After the loss is calculated, the internal variables (weights and biases) of all the layers of the neural network are adjusted, so as to minimize this loss — that is, to make the output value closer to the correct value.

![1](https://user-images.githubusercontent.com/65876994/101147914-5540c300-3660-11eb-84f9-a4ba9bf97e6e.PNG)
![2](https://user-images.githubusercontent.com/65876994/101148028-7ef9ea00-3660-11eb-9f73-100e4b502399.PNG)


### Basic terms
- Feature: The input(s) to our model
- Examples: An input/output pair used for training
- Labels: The output of the model
- Layer: A collection of nodes connected together within a neural network.
- Model: The representation of your neural network
- Dense and Fully Connected (FC): Each node in one layer is connected to each node in the previous layer.
- Weights and biases: The internal variables of model
- Loss: The discrepancy between the desired output and the actual output
- MSE: Mean squared error, a type of loss function that counts a small number of large discrepancies as worse than a large number of small ones.
- Gradient Descent: An algorithm that changes the internal variables a bit at a time to gradually reduce the loss function.
- Optimizer: A specific implementation of the gradient descent algorithm. (There are many algorithms for this. In this course we will only use the “Adam” Optimizer, - which stands for ADAptive with Momentum. It is considered the best-practice optimizer.)
- Learning rate: The “step size” for loss improvement during gradient descent.
- Batch: The set of examples used during training of the neural network
- Epoch: A full pass over the entire training dataset
- Forward pass: The computation of output values from input
- Backward pass (backpropagation): The calculation of internal variable adjustments according to the optimizer algorithm, starting from the output layer and working back through each layer to the input.

