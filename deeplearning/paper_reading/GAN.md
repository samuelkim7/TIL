## Generative Adversarial Nets
Ian J. Goodfellow, ...

## Introduction
- The generative model can be thought of as analogous to a team of counterfeiters, trying to produce fake currency and use it without detection, while the discriminative model is analogous to the police, trying to detect the counterfeit currency. 
- Competition in this game drives both teams to improve their methods until the counterfeits are indistiguishable from the genuine articles.
- In this case, we can train both models using only the highly successful backpropagation and dropout algorithms [17] and sample from the generative model using only forward propagation.

### 기본 배경지식
- 확률분포: 확률 변수가 특정한 값을 가질 확률을 나타내는 함수
- 이산확률분포: 확률변수 X의 개수를 셀 수 있을 때. 예를 들어 주사위 눈금 X의 확률분포
- 연속확률분푀: 확률변수 X의 개수를 정확히 셀 수 없을 때. 확률 밀도 함수를 통해 분포를 표현. 키, 달리기 성적 등이 예시임
  - 실제 세계의 많은 데이터는 정규분포로 표현될 수 있음
- 이미지 데이터는 다차원 공간 상의 한 점으로 표현됨. 이미지의 분포를 근사하는 모델을 학습시킬 수 있음
- 이미지 데이터에 대한 확률분포: 이미지에서의 다양한 특징들이 각각의 확률변수가 되는 분포. 다변수 확률분포

### 생성모델
- 실존하지 않지만 있을 법한 이미지를 생성할 수 있는 모델. 각각의 클래스에 대한 다변수 확률 분포를 학습하는 모델
- 결국 실제 이미지 데이터의 분포를 근사하는 모델을 만드는 것이 목표임
- 따라서 학습이 잘 되었다면 통계적으로 평균적인 특징을 가지는 데이터를 쉽게 생성할 수 있음

### GAN
- generator와 discriminator 두 개의 네트워크를 함께 학습하면서 generator를 발전시킴
- generator: make new data instance. 생성한 이미지가 discriminator에 의해서 real 이미지로 인식되도록 학습을 진행함
- discriminator: predict if the sample is from the real distribution (real: 1 ~ fake: 0). real 이미지와 fake 이미지를 받아서 각각 1과 0을 부여할 수 있도록 학습을 진행함
- 실제 프로그램 상에서는 각각의 mini-batch 마다 G, D 순으로 학습하거나 D, G 순으로 학습을 진행함
