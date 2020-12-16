### DNN
- An activation function is simply some function we apply to each of a layer's outputs.
- A common loss function for regression problems is the mean absolute error or MAE. For each prediction y_pred, MAE measures the disparity from the true target y_true by an absolute difference abs(y_true - y_pred).
- Besides MAE, other loss functions you might see for regression problems are the mean-squared error (MSE) or the Huber loss.

### hyperparameter
- The learning rate and the size of the minibatches are the two parameters that have the largest effect on how the SGD training proceeds.
- With the learning rate and the batch size, you have some control over:
  - How long it takes to train a model
  - How noisy the learning curves are
  - How small the loss becomes
- You probably saw that smaller batch sizes gave noisier weight updates and loss curves. This is because each batch is a small sample of data and smaller samples tend to give noisier estimates. Smaller batches can have an "averaging" effect though which can be beneficial. Smaller learning rates make the updates smaller and the training takes longer to converge. Large learning rates can speed up training, but don't "settle in" to a minimum as well. When the learning rate is too large, the training can fail completely.

### SGD
- The optimizer is an algorithm that adjusts the weights to minimize the loss.
- SGD: Virtually all of the optimization algorithms used in deep learning belong to a family called stochastic gradient descent. Stochastic means "determined by chance." Our training is stochastic because the minibatches are random samples from the dataset.
- Adam is an SGD algorithm that has an adaptive learning rate that makes it suitable for most problems without any parameter tuning (it is "self tuning", in a sense). Adam is a great general-purpose optimizer.
#### plotting loss
```python
history_df = pd.DataFrame(history.history)
history_df['loss'].plot();
```
