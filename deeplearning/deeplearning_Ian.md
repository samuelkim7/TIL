## Chapter 5 Machine Learning Basics

- Definition of Meachine Learning by Mitchell: A computer program that learns Experience E with respect to Task T and Performance P
  - Experience E 
    - Most machine learning algorithms simply experience a dataset. A dataset is a collection of examples, which are in turn collections of features.
    - With these kinds of learning algorithms: Unsupervised Learning / Supervised Learning / Reinforcement Learning 

#### Challenges Motivating Deep Learning

- The Curse of Dimensionality
  - Many machine learning problems become exceedingly diﬃcult when the number of dimensions in the data is high, because the number of possible conﬁgurations of x will be much larger than the number of training examples in this case.

- Manifold Learning
  - A manifold is a connected region. Mathematically, it is a set of points associated with a neighborhood around each point.
  - Manifold learning assumes that most of R^n consists of invalid inputs, and that interesting inputs occur only along a collection of manifolds containing a small subset of points, with interesting variations in the output of the learned function occurring only along directions that lie on the manifold.
