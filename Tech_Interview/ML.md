### 확률 / 통계 / 수학
- 선형 대수: 선형성을 가지는 대수로 이루어진 방정식들의 해를 구하는 방법론 혹은 학문
- 고유값(eigen value)와 고유벡터(eigen vector)에 대해 설명해주세요.  
정방행렬 A를 벡터 x에 곱했을 때 변환된 전과 후가 평행할 경우 x를 고유벡터라고 한다. 이 때 변환된 크기의 정도를 고유값이라고 한다.

- 리샘플링일란  
리샘플링은 내가 가지고 있는 샘플에서 다시 샘플 부분집합을 뽑아서 통계량의 변동성을 확인하는 것. 대표적인 예로 K-fold cross validation이 있음

- 확률 및 통계: 확률은 주어준 표본 공간에서 발생할 수 있는 사건들 중 각 사건이 일어날 가능성을 추정하는 것. 즉 불확실한 미래에 발생할 사건을 예측하기 위한 방법론. 통계는 수집된 표본 데이터들을 기반으로 전체 데이터 집합의 분포를 추정하는 것
- 확률변수: 표본 공간의 각 사건에 하나의 실수를 대응시키는 변수 / 이산확률 변수: 확률변수가 취할 수 있는 값이 정수인 경우 / 연속 확률 변수: 확률변수가 취할 수 있는 값이 실수인 경우
- 확률함수: 확률변수 X를 0과 1 사이의 확률로 mapping하는 함수
- 확률분포: 확률 변수가 특정한 값을 가질 확률을 나타내는 함수. 확률변수에 따라 확률이 어떻게 흩어져 있는지를 표현함
- 기댓값: 어떤 확률을 가진 사건을 무한히 반복했을 경우 얻을 수 있는 값의 평균. x와 P(x)의 곱의 시그마 값 / 분산: X에서 기댓값을 뺀 편차의 제곱. 확률분포가 평균으로부터 얼마나 산포되어 있는지를 표현함
- 공분산: 확률변수 X와 Y에 대해 X가 변할 때 Y가 변하는 정도를 나타내는 값. 두 확률변수의 관계를 보여주는 값. 편차의 곱의 기댓값으로 구하며 두 사건이 독립일 경우 공분산은 0임
- 상관계수: 측정단위와 상관 없이 두 확률 변수의 상관성을 보여주는 값. 공분산을 두 확률변수가 갖는 표준편차의 곲으로 나눈 값
- 조건부 확률: 주어진 사건이 일어났다는 가정 하에 다른 한 사건이 일어날 확률. P(B|A) = P(A and B) / P(A)
- 평균과 중앙값: 평균은 관측치의 총합을 관측치의 개수로 나누어 구함. 평균은 확률분포가 얼마나 퍼져있는지에 대한 정보는 주지 않는다. / 중앙값: 절반 이상의 값이 이 값 보다 크거나 같고 나머지 절반의 값이 이 값 보다 작거나 같은 값. 확률분포 상에서 면적을 양분함. 중앙값은 평균과 달리 극단적인 값들의 영향을 받지 않음
- 중심극한정리  
모집단이 평균이 m이고 표준편차가 s인 임의의 분포를 이룬핟고 할 때, 이 모집단으로부터 추출된 표분의 크기 n이 충분히 크다면 표본 "평균들의 분포"는 평균이 m이고 표준편차가 s / sqrt(s) 인 정규분포에 근접한다. 수집한 표본들의 통계량을 이용해서 모집단의 모수를 추정할 수 있는 확률적 근거를 마련해 줌

### 머신러닝
- Cross Validation  
overfitting을 막기 위해서 데이터 세트를 여러 조합의 훈련 및 검증 세트로 나누어서 모델 학습과 평가를 수행하는 것. K-fold cross validation이 대표적임. Stratified k-fold는 불균형이 큰 경우에 사용하는 방법으로서 전체 데이터셋의 레이블이 지닌 분포를 반영하여 k-fold를 나누는 것임
- 성능 평가 metric  
