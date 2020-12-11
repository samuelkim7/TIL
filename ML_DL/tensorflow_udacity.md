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
  - Gradient Descent: After the loss is calculated, the internal variables (weights and biases) of all the layers of the neural network are adjusted, so as to minimize this loss — that is, to make the output value closer to the correct value. <a href=https://developers.google.com/machine-learning/crash-course/reducing-loss/video-lecture>more detail</a>

<img src=https://user-images.githubusercontent.com/65876994/101147914-5540c300-3660-11eb-84f9-a4ba9bf97e6e.PNG height=400> <br>
<img src=https://user-images.githubusercontent.com/65876994/101148028-7ef9ea00-3660-11eb-9f73-100e4b502399.PNG height=400> 


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

### dense layer
- The neurons in one layer are fully connected to the neurons in the previous layer.
- The training process only changes the w and b variables to be able to match the input to the output. 
- Without knowing the target algorithm, we just give a model a number of layers and weights to tune. Then the model will figure out the best algorithm that maps the input to the output.

## Fashion MNIST
In this lesson we trained a neural network to classify images of articles of clothing. To do this we used the Fashion MNIST dataset, which contains 70,000 greyscale images of articles of clothing. We used 60,000 of them to train our network and 10,000 of them to test its performance. In order to feed these images into our neural network we had to flatten the 28 × 28 images into 1d vectors with 784 elements. Our network consisted of a fully connected layer with 128 units (neurons) and an output layer with 10 units, corresponding to the 10 output labels. These 10 outputs represent probabilities for each class. The softmax activation function calculated the probability distribution.

### Basic terms
- Flattening: The process of converting a 2d image into 1d vector
- ReLU: An activation function that allows a model to solve nonlinear problems
- Softmax: A function that provides probabilities for each possible output class
- Classification: A machine learning model used for distinguishing among two or more output categories

### The Rectified Linear Unit (ReLU)
- ReLU stands for Rectified Linear Unit and it is a mathematical function that looks like this:
<img src=https://user-images.githubusercontent.com/65876994/101150969-570c8580-3664-11eb-95a9-82a711092351.PNG height=300>
- As we can see, the ReLU function gives an output of 0 if the input is negative or zero, and if input is positive, then the output will be equal to the input.
- ReLU is a type of activation function. There several of these functions (ReLU, Sigmoid, tanh, ELU), but ReLU is used most commonly and serves as a good default.   
- <a href=https://www.kaggle.com/dansbecker/rectified-linear-units-relu-in-deep-learning>more detail</a>

### Training and Testing
- Training Set: The data used for training the neural network.
- Test set: The data used for testing the final performance of our neural network.
- The test dataset was used to try the network on data it has never seen before. This enables us to see how the model generalizes beyond what it has seen during training, and that it has not simply memorized the training examples.

### Classification and Regression
- Regression: A model that outputs a single value. For example, an estimate of a house’s value.
- Classification: A model that outputs a probability distribution across several categories. For example, in Fashion MNIST, the output was 10 probabilities, one for each of the different types of clothing. Remember, we use Softmax as the activation function in our last Dense layer to create this probability distribution.

<img src=https://user-images.githubusercontent.com/65876994/101155450-832b0500-366a-11eb-9a92-6a9ada3b86e3.PNG height=300>

## Introduction to CNNs
### basic terms
- CNNs: Convolutional neural network. That is, a network which has at least one convolutional layer. A typical CNN also includes other types of layers, such as pooling layers and dense layers.
- Convolution: The process of applying a kernel (filter) to an image
- Kernel / filter: A matrix which is smaller than the input, used to transform the input into chunks
- Padding: Adding pixels of some value, usually 0, around the input image
- Pooling The process of reducing the size of an image through downsampling.There are several types of pooling layers. For example, average pooling converts many values into a single value by taking the average. However, maxpooling is the most common.
- Maxpooling: A pooling process in which many values are converted into a single value by taking the maximum value from among them.
- Stride: the number of pixels to slide the kernel (filter) across the image.
- Downsampling: The act of reducing the size of an image

### Techniques to Prevent Overfitting
- Early Stopping: In this method, we track the loss on the validation set during the training phase and use it to determine when to stop training such that the model is accurate but not overfitting.
- Image Augmentation: Artificially boosting the number of images in our training set by applying random image transformations to the existing images in the training set.
- Dropout: Removing a random selection of a fixed number of neurons in a neural network during training.

### CNN summary
- Resizing: When working with images of different sizes, you must resize all the images to the same size so that they can be fed into a CNN.
- Color Images: Computers interpret color images as 3D arrays.
- RGB Image: Color image composed of 3 color channels: Red, Green, and Blue.
- Convolutions: When working with RGB images we convolve each color channel with its own convolutional filter. Convolutions on each color channel are performed in the same way as with grayscale images, i.e. **by performing element-wise multiplication of the convolutional filter (kernel) and a section of the input array**. The result of each convolution is added up together with a bias value to get the convoluted output.
- Max Pooling: When working with RGB images we perform max pooling on each color channel using the same window size and stride. Max pooling on each color channel is performed in the same way as with grayscale images, i.e. by selecting the max value in each window.
- Validation Set: We use a validation set to check how the model is doing during the training phase. Validation sets can be used to perform **Early Stopping to prevent overfitting** and can also be used to help us **compare different models and choose the best one**.

## Transfer Learning
- Transfer Learning: A technique that reuses a model that was created by machine learning experts and that has already been trained on a large dataset. When performing transfer learning we must always change the last layer of the pre-trained model so that it has the same number of classes that we have in the dataset we are working with.
- Freezing Parameters: Setting the variables of a pre-trained model to non-trainable. By freezing the parameters, we will ensure that only the variables of the last classification layer get trained, while the variables from the other layers of the pre-trained model are kept the same.
- MobileNet: A state-of-the-art convolutional neural network developed by Google that uses a very efficient neural network architecture that minimizes the amount of memory and computational resources needed, while maintaining a high level of accuracy. MobileNet is ideal for mobile devices that have limited memory and computational resources.
