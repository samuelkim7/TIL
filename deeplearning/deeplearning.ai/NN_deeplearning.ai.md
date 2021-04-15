### Logistic Regression
- Being able to implement your algorithms without using explicit for loops is really important and will help you to scale to much bigger datasets.
- For this, Vectorization is needed. On a large dataset, this is very important for computational efficiency.
- Whenever possible, **avoid explicit for-loops.**
  - use np.dot() / np.exp() / np.log() / np.maximum()

### numpy for deeplearning
- np.exp(x) works for any np.array x and applies the exponential function to every coordinate
- the sigmoid function and its gradient
- image2vector is commonly used in deep learning
- np.reshape is widely used. In the future, you'll see that keeping your matrix/vector dimensions straight will go toward eliminating a lot of bugs. 
- numpy has efficient built-in functions
- broadcasting is extremely useful
- np.dot([1,2,3],[1,2,3]) = 14

### pre-processing image dataset
Common steps for pre-processing a new dataset are:  
- Figure out the dimensions and shapes of the problem (m_train, m_test, num_px, ...)
- Reshape the datasets such that each example is now a vector of size (num_px * num_px * 3, 1)
- "Standardize" the data

### activation functions
- tanh is always better than sigmoid. (having the mean of 0 -> centerizing data)
- For binary classification in the output layer, we can use sigmoid function. otherwise never use it.
- recified linear unit (ReLU): a = max(0, z). 
  - Usually in practice, we just use the ReLU. This makes your model learn much faster.
  - the two above makes learning slower because of the slope becomes zero as |z| becomes bigger.
- leaky ReLU: a = max(0.01z, z). Works little bit better than ReLU. But in practice this is not that much used.
- when you don't know what to use, then try them all and evaluate them.
- linear activation function is never used except for the output layer in a regression problem.
<br>

#### derivaties
- sigmoid : dz = a(1-a)
- tanh : dz = 1 - a^2
- ReLU: 0 or 1 (undefined at z=0. In software, it's okay to consider it as 0.)
- leaky ReLU: 0.01 or 1

### Random initialization
- W should be initialized as random Gaussian numbers for model's learning. And in case of using sigmoid or tanh function, w should be small (\*0.01) for better learning.
  - np.random.randn(m,n)
- b is okay to be initialized as zero.
  - nmp.zeros(m,1)

### Momentum
- There's an algorithm called momentum, or gradient descent with momentum that almost always works faster than the standard gradient descent algorithm. In one sentence, the basic idea is to compute an exponentially weighted average of your gradients, and then use that gradient to update your weights instead.
