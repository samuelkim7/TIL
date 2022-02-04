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

## BatchNormalization


## Optimizers

## Major models
