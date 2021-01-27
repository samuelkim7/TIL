### Feature Extraction
- The feature extraction performed by the base consists of three basic operations:
  - **Filter** an image for a particular feature (convolution)
  - **Detect** that feature within the filtered image (ReLU)
  - **Condense** the image to enhance the features (maximum pooling)
  
### Weights
- The weights a convnet learns during training are primarily contained in its convolutional layers. These weights we call kernels.
- A kernel operates by scanning over an image and producing a weighted sum of pixel values. 
- In this way, a kernel will act sort of like a polarized lens, emphasizing or deemphasizing certain patterns of information.
- The kernels in a convolutional layer determine what kinds of features it creates. 
- During training, a convnet tries to **learn what features it needs** to solve the classification problem. This means **finding the best values for its kernels**.

### ReLU
- The ReLU activation says that negative values are not important and so sets them to 0. ("Everything unimportant is equally unimportant.")

### Maximum pooling
- When applied after the ReLU activation, it has the effect of "intensifying" features. The pooling step increases the proportion of active pixels to zero pixels.
- The zero-pixels carry positional information. When MaxPool2D removes some of these pixels, it removes some of the positional information in the feature map. This gives a convnet a property called **translation invariance**.

### Global average pooling
- But, instead of "unstacking" the feature (like Flatten), Global average pooling simply replaces the entire feature map with its average value.
- Global average pooling is often used in modern convnets. One big advantage is that it greatly reduces the number of parameters in a model, while still telling you if some feature was present in an image or not.
