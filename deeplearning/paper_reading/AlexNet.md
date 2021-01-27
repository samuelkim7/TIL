## ImageNet Classification with Deep Convolutional Neural Networks
- Krizhevsky, A., Sutskever, I., and Hinton, G. E.

### Introduction
-  Luckily, current GPUs, paired with a highly-optimized implementation of 2D convolution, are powerful enough to facilitate the training of interestingly-large CNNs, and recent datasets such as ImageNet contain enough labeled examples to train such models without severe overfitting.

### Architecture
#### ReLU
- Deep convolutional neural networks with ReLUs train several times faster than their equivalents with tanh units.

#### Overall
- The net contains eight layers with weights; the first five are convolutional and the remaining three are fully-connected.

### Reduce Overfitting
#### Data Augmentation
- The first form of data augmentation consists of generating image translations and horizontal reflections.

#### Dropout
- The recently-introduced technique, called “dropout” [10], consists of setting to zero the output of each hidden neuron with probability 0.5. The neurons which are
“dropped out” in this way do not contribute to the forward pass and do not participate in back-propagation.

#### Details of learning
- We trained our models using stochastic gradient descent with a batch size of 128 examples, momentum of 0.9, and weight decay of 0.0005.

### Discussion
- Our results show that a large, deep convolutional neural network is capable of achieving record-breaking results on a highly challenging dataset using purely supervised learning. It is notable that our network’s performance degrades if a single convolutional layer is removed.
