## Very Deep Convolutional Networks for Large-Scale Image Recognition
Karen Simonyan & Andrew Zisserman

### Introduction
- In this paper, we address another important aspect of ConvNet architecture design – its depth.
- To this end, we fix other parameters of the architecture, and steadily increase the depth of the network by adding more convolutional layers, which is feasible due to the use of very small (3 × 3) convolution filters in all layers.

### ConvNet Configurations
- All our ConvNet layer configurations are designed using the same principles, inspired by Ciresan et al. (2011); Krizhevsky et al. (2012).

#### Architecture
- The convolution stride is fixed to 1 pixel; the spatial padding of conv. layer input is such that the spatial resolution is preserved after convolution, i.e. the padding is 1 pixel for 3 × 3 conv. layers.
- Max-pooling is performed over a 2 × 2 pixel window, with stride 2.
- A stack of convolutional layers (which has a different depth in different architectures) is followed by
three Fully-Connected (FC) layers. 

### Classification Framework
- The batch size was set to 256, momentum to 0.9. The training was regularised by weight decay (the L 2 penalty multiplier set to 5 · 10−4) and dropout regularisation for the first two fully-connected layers (dropout ratio set to 0.5) 
- The learning rate was initially set to 10−2, and then decreased by a factor of 10 when the validation set accuracy stopped improving. 

### Classification Experiments
- Notably, we did not depart from the classical ConvNet architecture of LeCun et al. (1989), but improved it by substantially increasing the depth.
