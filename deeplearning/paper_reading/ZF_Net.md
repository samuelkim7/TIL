## Visualizing and Understanding Convolutional Networks

## Introduction
- Deconvnet:  a novel way to map these activities back to the input pixel space. 
- A deconvnet can be thought of as a convnet model that uses the same components (filtering, pooling) but in reverse, so instead of mapping pixels to features does the opposite.
- To examine a convnet, a deconvnet is attached to each of its layers.

## Results
- The smaller stride (2 vs 4) and filter size (7x7 vs 11x11) results in more distinctive features and fewer “dead” features.

## Discussion
- Features are not random uninterpretable patterns. Rather, they show many intuitively desirable properties such as compositionality, increasing invariance and class discrimination as we ascend the layers.
- Finally, we showed how the ImageNet trained model can generalize well to other datasets.
