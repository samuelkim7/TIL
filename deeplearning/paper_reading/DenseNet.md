

### Introduction
- each layer obtains additional inputs from all preceding layers and passes on its own feature-maps to all subsequent layers.
- Crucially, in contrast to ResNets, we never combine features through summation before they are passed into a layer; instead, we combine features by concatenating them.
- Each layer has direct access to the gradients from the loss function and the original input signal, leading to an implicit deep supervision.
- Concatenating feature-maps learned by different layers increases variation in the input of subsequent layers and improves efficiency. This constitutes a major difference between DenseNets and ResNets.
- a 1×1 convolution can be introduced as bottleneck layer before each 3×3 convolution to reduce the number of input feature-maps, and thus to improve computational efficiency.
- 
