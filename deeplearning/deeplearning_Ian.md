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
- 
