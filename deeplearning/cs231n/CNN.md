## CNN
- convolution: taking a filter, sliding it spatially over the image, and computiong the dot product at every location
- keeping the image structure
- one filter results in one activation map and represents one pattern in the input.
- Stacked convolutional layers gradully represent more complex features in the input.
- Output size: (N - F) / stride + 1
- CNN layer: Each neuron looks at the local spatial region. Activation value means "how much a neuron fired in this position".
- cf) Fully-Connected Layer: Each neuron looks at the full input volume
-  Pooling layer
  - down sampling
  - Output size: (N - F) / stride + 1

## Training Neural Networks
### Activation Functions

#### Sigmoid
- squashes numbers to range [0, 1]
- "saturating firing rate"
- Problems
  - Saturated neurons "kill" the gradients
  - Sigmoid outputs are not zero-centered
  - exp() is a bit compute expensive

#### tanh
- Squashes numbers to range [-1, 1]
- zero centered (nice)
- still kills gradients when saturated.

#### ReLU
- f(x) = max(0, x)
- Does not saturate (in + region)
- Very computationally efficient
- Converges much faster than sigmoid/tanh in practice (e.g. 6x)
- Actually more biologically plausible than sigmoid
- Problems
  - Not zero-centered output
  - killing the gradient in - region

#### Leaky ReLU
- f(x) = max(0.01x, x)
- will not "die".
- cf) Parametric Rectifier (PReLU)
  - f(x) = max(ax, x)

#### ELU (Exponential Linear Units)
- f(x) = x if x > 0  / a(exp(x) - 1) if x < 0
- Closer to zero mean outputs
- Negative saturation regime adds some robustness to noise
