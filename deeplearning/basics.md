## Regularization
- Norm 은 벡터의 크기(혹은 길이)를 측정하는 방법(혹은 함수)
- L1 Norm 은 벡터 p, q 의 각 원소들의 차이의 절대값의 합
- L2 Norm 은 벡터 p, q 의 유클리디안 거리(직선 거리)
- cf)  L1 Loss: 실제 값과 예측치 사이의 차이(오차) 값의 절대값을 구하고 그 오차들의 합 / L2 Loss: 오차의 제곱의 합. Outlier에 더 큰 영향을 받음
- L1 regularization: 기존 loss function에 가중치의 절대값을 더해줌. 편미분 후에는 결국 w에서 특정 상수값을 빼주면서 업데이트를 하게 됨으로 몇몇 중요한 가중치들만 남기게 됨
- L2 regularzation: 기존 loss function에 가중치의 제곱을 더함


## Dropout
- Based on Dropout: A Simple Way to Prevent Neural Networks from Overfitting (2014, JMLR)
- The key idea is to randomly drop units (along with their connections) from the neural network during training.
- During training, dropout samples from an exponential number of different “thinned” networks.
- At test time, it is easy to approximate the effect of averaging the predictions of all these thinned networks by simply using a single unthinned network that has smaller weights. 
- Dropout prevents overfitting and provides a way of approximately combining exponentially many different neural network architectures efficiently.
