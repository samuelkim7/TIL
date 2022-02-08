## Chapter 3 Probability and Information Theory
### Basics
- While probability theory allows us to make uncertain statements and to reasonin the presence of uncertainty, information theory enables us to quantify the amountof uncertainty in a probability distribution.
- Random Variables
  - A random variable is a variable that can take on different values randomly.
  - On its own, a random variable is just a description of the states that are possible; it must be coupled with a probability distribution that speciﬁes how likely each of these states are.
- Probability Distributions
  - Probability mass function (PMF)
    - For discrete random variables
    - The probability mass function maps from a state of a random variable tothe probability of that random variable taking on that state.
  - Probability density function (PDF)
    - For continuous random variables
    - The probability of landing inside an inﬁnitesimal region withvolume δx is given by p(x)δx.
- Expectation, Variance and Covariance
  - The expectation, or expected value, of some function f(x) with respect to a probability distribution P(x) is the average, or mean value, that f takes on when x is drawn from P. For continuous variables, it is computed with an integral.
  - The variance gives a measure of how much the values of a function of a random variable x vary as we sample different values of x from its probability distribution.
  - The covariance gives some sense of how much two values are linearly related to each other, as well as the scale of these variables.
  - If the sign of the covariance is positive, then both variables tend to take on relatively high values simultaneously. If the sign of the covariance is negative, then one variable tends totake on a relatively high value at the times that the other takes on a relatively low value and vice versa.
 ![image](https://user-images.githubusercontent.com/65876994/152912058-6c8dda4c-174f-4caa-b58d-84d60af3f0c5.png)

### Common Probability Distributions
- Gaussian Distribution
  - 

## Chapter 4 Numerical Computation
- Gradient-Based Optimization
  - **Optimization** refers to the task of either minimizing or maximizing some functionf(x) by altering x.
  - The function we want to minimize or maximize is called the objective function, or criterion. When we are minimizing it, we may also call it the cost function,loss function, or error function.
  - We can thus reduce f(x) by moving x in small steps with the opposite sign of the derivative. This technique is called **gradient descent**.
  - Points where f(x) = 0 are known as critical points, or stationary points. A **local minimum** is a point where f(x) is lower than at all neighboring points, so it is no longer possible to decrease f(x) by making inﬁnitesimal steps.
  - Some critical points are neither maxima nor minima. These are known as **saddle points**.
  - A point that obtains the absolute lowest value of f(x) is a global minimum.
  - The **second derivative** tells us how the ﬁrst derivative will change as we vary the input. This is important because it tells us whether a gradient step will cause as much of an improvementas we would expect based on the gradient alone. We can think of the second derivative as measuring curvature.

## Chapter 5 Machine Learning Basics

#### Learning Algorithms
- Definition of Meachine Learning by Mitchell: A computer program that learns Experience E with respect to Task T and Performance P
  - Experience E 
    - Most machine learning algorithms simply experience a dataset. A dataset is a collection of examples, which are in turn collections of features.
    - With these kinds of learning algorithms: Unsupervised Learning / Supervised Learning / Reinforcement Learning 

#### Building a Machine Learning Algorithm
- Nearly all deep learning algorithms can be described as particular instances of a fairly simple **recipe**: combine a speciﬁcation of a dataset, a cost function, an optimization procedure and a model.

#### Challenges Motivating Deep Learning
- The Curse of Dimensionality
  - Many machine learning problems become exceedingly diﬃcult when the number of dimensions in the data is high, because the number of possible conﬁgurations of x will be much larger than the number of training examples in this case.

- Manifold Learning
  - A manifold is a connected region. Mathematically, it is a set of points associated with a neighborhood around each point.
  - Manifold learning assumes that most of R^n consists of invalid inputs, and that **interesting inputs occur only along a collection of manifolds** containing a small subset of points, with interesting variations in the output of the learned function occurring only along directions that lie on the manifold.
  - The ﬁrst observation in favor of the manifold hypothesis is that the probability distribution over images, text strings, and sounds that occur in real life is **highly concentrated**.
  - Another point that needs to be established: the examples we encounter are connected to each other by other examples, with each example surrounded by other highly similar examples that can be reached by applying transformations to traverse the manifold.
  - When the data lies on a low-dimensional manifold, it can be most natural for machine learning algorithms to represent the data in terms of coordinates on the manifold, rather than in terms of coordinates in R^n.


## Chapter 6 Deep Feedforward Networks
- The model is associated with a directed acyclic graph describing how the functions are composed together.
- The largest diﬀerence between the linear models we have seen so far and neural networks is that the **nonlinearity** of a neural network causes most interesting loss functions to become nonconvex.
- Stochastic gradient descent applied to nonconvex loss functions has **no such convergence guarantee** and is sensitive to the values of the initial parameters.

- Cost functions
  - 
