### Tensors
- Tensors on the CPU and NumPy arrays can share their underlying memory locations, and changing one will change the other.

### torch.autograd

### Neural Network
- torch.Tensor - A multi-dimensional array with support for autograd operations like backward().
- nn.Module - Neural network module. Convenient way of encapsulating parameters, with helpers for moving them to GPU, exporting, loading, etc.

#### Loss function
