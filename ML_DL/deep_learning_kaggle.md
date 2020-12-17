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
- SGD: Virtually all of the optimization algorithms used in deep learning belong to a family called stochastic gradient descent. Stochastic means "determined by chance." Our training is **stochastic** because the minibatches are random samples from the dataset.
- Adam is an SGD algorithm that has an adaptive learning rate that makes it suitable for most problems without any parameter tuning (it is "self tuning", in a sense). Adam is a great general-purpose optimizer.
#### plotting loss
```python
history_df = pd.DataFrame(history.history)
history_df['loss'].plot();
```

### Underfitting and Overfitting
- Underfitting the training set is when the loss is not as low as it could be because the model hasn't learned enough signal. Overfitting the training set is when the loss is not as low as it could be because the model learned too much noise. The trick to training deep learning models is finding the best balance between the two.
- A model's **capacity** refers to the size and complexity of the patterns it is able to learn. For neural networks, this will largely be determined by how many neurons it has and how they are connected together. If it appears that your network is underfitting the data, you should try increasing its capacity.
- You can increase the capacity of a network either by making it wider (more units to existing layers) or by making it deeper (adding more layers). Wider networks have an easier time learning more linear relationships, while deeper networks prefer more nonlinear ones. Which is better just depends on the dataset.

#### Early Stopping
- We can simply stop the training whenever it seems the validation loss isn't decreasing anymore. Interrupting the training this way is called early stopping.
```python
from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(
    min_delta=0.001, # minimium amount of change to count as an improvement
    patience=20,     # how many epochs to wait before stopping
    restore_best_weights=True,
)
```
- "If there hasn't been at least an improvement of 0.001 in the validation loss over the previous 20 epochs, then stop the training and keep the best model you found."

### Dropout and BatchNormalization
#### Dropout
- In Keras, the dropout rate argument rate defines what percentage of the input units to shut off. Put the Dropout layer just before the layer you want the dropout applied to.

#### BatchNormalization
- A batch normalization layer looks at each batch as it comes in, first normalizing the batch with its own mean and standard deviation, and then also putting the data on a new scale with two trainable rescaling parameters. Batchnorm, in effect, performs a kind of coordinated rescaling of its inputs.
- Models with batchnorm tend to need **fewer epochs to complete training**. Moreover, batchnorm can also **fix various problems** that can cause the training to get "stuck".
- You can put it after a layer or between a layer and its activation function.
