## Regularization
- Norm 은 벡터의 크기(혹은 길이)를 측정하는 방법(혹은 함수)
- L1 Norm 은 벡터 p, q 의 각 원소들의 차이의 절대값의 합
- L2 Norm 은 벡터 p, q 의 유클리디안 거리(직선 거리)
- cf)  L1 Loss: 실제 값과 예측치 사이의 차이(오차) 값의 절대값을 구하고 그 오차들의 합 / L2 Loss: 오차의 제곱의 합. Outlier에 더 큰 영향을 받음
- L1 regularization: 기존 loss function에 가중치의 절대값을 더해줌. 편미분 후에는 결국 w에서 특정 상수값을 빼주면서 업데이트를 하게 됨으로 몇몇 중요한 가중치들만 남기게 됨
- L2 regularzation: 기존 loss function에 가중치의 제곱을 더함


## Dropout
- Overfitting에 대한 해결책으로는 학습 데이터를 늘리거나 regularization을 적용하는 방법이 있다. dropout은 regularization 기법 중 하나이다. 단순히 말해서 NN이 지닌 일부 유닛들을 생략하고 학습을 진행하는 기법이다. 모델 ensemble의 장점을 취하는 방식으로 훈련하고 테스트시에는 간단한 방식으로 평균을 적용하게 된다.
- 테스트 시에는 생략을 없애고 각각의 뉴런들이 존속할 확률을 가중치에 곱해서 (가중치는 더 작게 만들어서) inference를 수행한다.
- dropout을 적용한다는 것은 이전 뉴런의 출력값에 bernouli 확률변수를 곱해주는 것으로 볼 수 있다. 각각의 유닛에 대해 독립적으로 랜덤 변수가 곱해지기 때문에 n개의 유닛에 대해 총 2^n개의 조합이 가능하게 된다.
- dropout을 사용할 경우 학습 중 parameter들이 서로 의지하면서 학습이 되는 co-adaptation 현상을 방지하게 해준다. 특정 hidden unit이 다른 hidden unit들에 의존해서 실수를 바로잡을 수 없게 되기 때문이다. 이를 통해 dropout이 적용된 NN은 좀 더 선명한 (salient) 특징을 추출하게 된다. 이것이 dropout이 지난 일반화 성능 향상 효과의 주된 요인일 것이다.
- 또한 dropout은 hidden unit들의 activation을 더 sparse하게 만든다. 
- dropout에서 dropout의 확률이 0.6 이상으로 지나치게 커지면 underfitting을 보이기도 하며, 반대로 0.2이하인 경우에는 overfitting이 다시 관찰된다.
- dropout을 적용할 경우 대부분의 이미지 벤치마크 데이터셋에서 신경망의 test 성능을 향상시키며 음성 및 텍스트 분야에서도 신경망의 성능을 개선시킨다. 
- Excerpts from paper - Based on Dropout: A Simple Way to Prevent Neural Networks from Overfitting (2014, JMLR)
  - The key idea is to randomly drop units (along with their connections) from the neural network during training.
  - During training, dropout samples from an exponential number of different “thinned” networks.
  - At test time, it is easy to approximate the effect of averaging the predictions of all these thinned networks by simply using a single unthinned network that has smaller weights. 
  - Dropout prevents overfitting and provides a way of approximately combining exponentially many different neural network architectures efficiently.

## Batch Normalization
- layer 수가 많은 NN 모델을 학습시키는 데 있어서 vanishing / exploiding gradient는 심각한 문제이다. 이것은 활성함수로 sigmoid나 tanh와 같은 non-linear saturating function을 사용할 경우 현저하게 발생한다. ReLU 활성함수로 어느정도 이것을 해결할 수 있지만 깊은 모델의 경우 여전히 이 문제가 발생한다.
- 따라서 성공적인 모델 학습을 위해서는 weight initialization, learning rate 선정, hyperparameter 설정에 많은 신경을 써야 한다. 
- internal covariate shift: 이전 layer의 parameter의 변화에 의해 현 layer의 입력 분포가 바뀌는 현상. 이를 해결하기 위한 단순한 방법으로는 각 layer로 들어가는 입력을 whitening (m=0, s=1) 시키는 것이다. 그러나 이 과정은 backpropagation과 상관 없이 진행되기 때문에 여전히 특정 parameter가 커지는 현상이 발생할 수 있다.
- BN은 mini-batch에 대하여 평균과 분산을 구한 뒤 정규화를 수행하고, 이를 다시 gamma와 beta를 통해 scaling과 shifting을 해주는 방식으로 수행된다. BN은 신경망에 포함되기 때문에 back propagation을 통해서 parameter와 함께 학습된다. 
- 테스트 시에는 훈련 시 계산한 모든 mini-batch들의 평균과 분산의 평균을 구해서 사용한다. 분산의 평균의 경우에는 보정을 위해서 m / m-1을 곱해준다. gamma와 beta의 경우 훈련된 값을 그대로 가져다가 사용한다.
- Normalizing the mean and standard deviation of a unit can reduce the expressive power of the neural network containing that unit. To maintain the expressive power of the network, it is common to replace the batch of hidden unit activations H with γH + β.
- The variables γ and β are learned parameters that allow the new variable to have any mean and standard deviation.
- The bias term should be omitted because it becomes redundant with the β parameter applied by the batch normalization reparametrization.

## Optimizers
#### Overview
- GD: 모든 데이터를 기반으로 내 위치의 기울기를 계산해서 움직임
- Momentum: 기울기를 기반으로 한 스텝을 움직인 후 관성을 따라서 더 움직임
- NAG: 먼저 관성 방향을 따라 움직인 후 움직인 자리에서 기울기를 기반으로 한 스텝 움직임
- SGD: mini-batch의 데이터를 기반으로 기울기를 산정해서 조금씩 움직임. 같은 시간에 더 많이 감
- Adagrad: 안 가본 곳은 더 빠르게 훑어보고 가본 곳은 보폭을 줄여서 세밀하게 탐색
- RMSProp: 이전 맥락을 고려해가면서 보폭을 줄임
- Adam: RMSProp + Momentum

#### Detail
- SGD
  - The most important property of SGD and related minibatch or online gradient-based optimization is that computation time per update does not grow with the number of training examples.
  - A noise is introduced in each step's gradient because of the random sampling of m training examples. So in practice, it is necessary to gradually decrease the learning rate over time.
  - The size of the step is simply the norm of the gradient multiplied by the learning rate.
- Momentum
  - The momentum algorithm accumulates an exponentially decaying moving average of past gradients and continues to move in their direction.
  - The velocity is set to an exponentially decaying average of the negative gradient.
  - A hyperparameter α (0 ~ 1) determines how quickly the contributions of previous gradients exponentially decay.
  - Now, the size of the step depends on how large and how aligned a sequence of gradients are.
- Nesterov Momentum
  - With Nesterov momentum, the gradient is evaluated after the current velocity is applied.
- AdaGrad
  - The AdaGrad algorithm individually adapts the learning rates of all model parameters by scaling them inversely proportional to the square root of the sum of all the historical squared values of the gradient.
  - The parameters with the largest partial derivative of the loss have a correspondingly rapid decrease in their learning rate, while parameters with small partial derivatives have a relatively small decrease in their learning rate.
  - The net effect is greater progress in the more gently sloped directions of parameter space.
  - AdaGrad shrinks the learning rate according to the entire history of the squared gradient and may have made the learning rate too small before arriving at such a convex structure.
- RMSProp
  - The RMSProp algorithm (Hinton, 2012) modiﬁes AdaGrad to perform better in the nonconvex setting by changing the gradient accumulation into an exponentially weighted moving average.
  - RMSProp uses an exponentially decaying average to discard history from the extreme past so that it can converge rapidly after ﬁnding a convex bowl.
  - Empirically, RMSProp has been shown to be an effective and practical op-timization algorithm for deep neural networks.
- Adam
  - The name “Adam” derives fromthe phrase “adaptive moments.” It is perhaps best seen as a variant on the combination of RMSProp and momentum with a few important distinctions.
  - First, in Adam, momentum is incorporated directly as an estimate of the ﬁrst-order moment (with exponential weighting) ofthe gradient.
  - Second, Adam includes bias corrections to the estimates of both the ﬁrst-order moments (the momentum term) and the (uncentered) second-order moments to account for their initialization at the origin. (학습 초기에 가중치들이 0으로 편향되는 경향을 보정함)

![image](https://user-images.githubusercontent.com/65876994/152711285-55c4adc0-a596-4f75-8bcc-8f815c356d5b.png)

- [참고 링크](https://hiddenbeginner.github.io/deeplearning/2019/09/22/optimization_algorithms_in_deep_learning.html)

## Major models
