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
