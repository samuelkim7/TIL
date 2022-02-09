### 확률 / 통계 / 수학
#### 기본개념
- 모집단: 연구자가 알고 싶어하는 집단 전체. 실제로는 너무 커서 다 관찰할 수 없음 / 표본: 연구자가 측정 또는 관찰한 결과들의 집합. 연구자는 표본을 관찰함으로써 모집단의 모수를 추정한다. / 표본공간: 실험의 모든 관찰 가능한 결과의 집합 / 사건: 표본공간의 부분 집합 / 확률 = (특정 사건의 경우의 수 / 표본공간의 크기)
- 확률 및 통계: 확률은 주어진 표본 공간에서 발생할 수 있는 사건들 중 각 사건이 일어날 가능성을 추정하는 것. 즉 불확실한 미래에 발생할 사건을 예측하기 위한 방법론. 통계는 수집된 표본 데이터들을 기반으로 전체 데이터 집합의 분포를 추정하는 것
- 확률변수: 표본 공간 상에서 확률적으로 발생하는 사건(모든 원소)에 실수를 대응시키는 함수 / 이산확률 변수: 확률변수가 취할 수 있는 값이 정수인 경우 / 연속 확률 변수: 확률변수가 취할 수 있는 값이 실수인 경우
- 확률함수: 확률변수 X를 0과 1 사이의 확률로 대응시키는 함수. 이를 이용해서 특정 사건이 일어날 확률을 계산할 수 있음. 이것을 도식화한 것이 바로 확률분포임 / 이산형인 경우 확률질량함수, 연속형인 경우 확률밀도함수라고 부름
- 확률의 공리: 특정 사건의 확률은 0과 1사이 / 표본공간 전체의 확률은 1 / 상호배타적인 모든 이벤트들의 합집합의 확률 = 각 이벤트들의 확률들의 합

#### 기본개념2
- 기댓값: 어떤 확률을 가진 사건을 무한히 반복했을 경우 얻을 수 있는 값의 평균. x와 P(x)의 곱의 시그마 값 / 분산: X에서 기댓값을 뺀 편차의 제곱들의 평균. 확률분포가 평균으로부터 얼마나 산포되어 있는지를 표현함. V(X) = E(X^2) - E(X)^2
- 공분산: 확률변수 X와 Y에 대해 X가 변할 때 Y가 변하는 정도를 나타내는 값. 두 확률변수의 관계를 보여주는 값. 편차의 곱의 기댓값으로 구하며 두 사건이 독립일 경우 공분산은 0임
- 상관계수: 측정단위와 상관 없이 두 확률 변수의 상관성을 보여주는 값. 공분산을 두 확률변수가 갖는 표준편차의 곲으로 나눈 값
- 조건부 확률: 주어진 사건이 일어났다는 가정 하에 다른 한 사건이 일어날 확률. P(B|A) = P(A and B) / P(A) / 반대로 교집합을 조건부 확률로 표현할 수 있음!
- 베이즈 룰: 사전확률과 사전정보 조건부확률로 사후확률을 예측하는 법칙
- 독립: P(B|A) = P(B) / P(AB) = P(A)P(B)
- 평균: 평균은 관측치의 총합을 관측치의 개수로 나누어 구함. 평균은 확률분포가 얼마나 퍼져있는지에 대한 정보는 주지 않는다. / 중앙값: 절반 이상의 값이 이 값 보다 크거나 같고 나머지 절반의 값이 이 값 보다 작거나 같은 값. 확률분포 상에서 면적을 양분함. 중앙값은 평균과 달리 극단적인 값들의 영향을 받지 않음
- 정규분포: 정규분포는 평균이 m, 표준편차가 s인 연속확률분포로서 평균에 가장 많은 데이터가 분포되어 있음 / Z-score: 데이터셋에서 평균을 빼고 표준편차로 나누어주어서 표준 정규 분포를 따르도록 한 개별 데이터 / 정규분포의 확률함수에 기반하여 정적분을 통해 특정 사건들의 확률을 계산할 수 있음. 이 값은 표준정규분포로 치환한 후 계산해도 동일함
- 중심극한정리  
모집단이 평균이 m이고 표준편차가 s인 임의의 분포를 이룬다고 할 때, 이 모집단으로부터 추출된 표분의 크기 n이 충분히 크다면 표본 "평균들의 분포"는 평균이 m이고 표준편차가 s / sqrt(s) 인 정규분포에 근접한다. 수집한 표본들의 통계량을 이용해서 모집단의 모수를 추정할 수 있는 확률적 근거를 마련해 줌

#### 기본개념3
- 확률분포: 확률함수로 부터 생성된 확률들의 패턴. 확률변수에 따라 확률이 어떻게 흩어져 있는지를 표현함
- 베르누이 확률변수: 두 가지 중 하나만 나오는 사건을 실수 0과 1에 대응시킨 확률변수 / 베르누이 확률함수: f(x;p) = p^x(1-p)^(1-x) / E(X) = p / V(X) = p(1-p) / 예시: 동전 던지기
- 베르누이 분포: 베르누이 확률함수로부터 생성된 확률들의 패턴
- 이항분포: 확률변수 X가 독립적인 베르누이 시행 n번에서의 총 성공 횟수로 주어질 때, 이 X의 확률함수가 생성한 패턴 / p(x) = nCx * p^x * (1-p)^(n-x) for x = 0, 1, ..., n / n과 p가 확률분포의 모양을 결정하는 모수임 / 베르누이 분포는 이항분포에서 n=1인 특수한 경우임
- Maximum Likelihood Estimation
  - 머신러닝을 주어진 데이터를 가장 잘 설명하는 '함수'를 찾는 과정이 아니라 가장 적절한 확률 분포의 parameter를 유추하는 과정으로 생각할 수 있음
  - 주어진 관측 데이터에 근거하여 가정된 확률 분포의 parameter를 추정하는 방법. Likelihood의 최대값을 찾는 방식으로 계산되며 여기서 likelihood는 관측 데이터가 가정된 분포로부터 나왔을 가능성을 의미한다. 결국 각 데이터 샘플에서 후보 분포에 대한 높이 (likelihood)를 계산해서 다 곱한 값이 likelihood function이 된다. 이 식의 결과 값이 가장 커지는 θ를 θ hat으로 추정하는 것이 가장 적합하다.
![image](https://user-images.githubusercontent.com/65876994/153129441-360c14ec-1750-4f8c-81d8-a92cc93bf16f.png)
  - 보통은 계산 상의 편의를 위해 위 식에 자연로그를 취해서 Log likelihood function의 최대값을 찾게 된다.
![image](https://user-images.githubusercontent.com/65876994/153129669-7d1d68e3-0210-4ae1-846e-376e34afe360.png)

#### 기타
- 선형 대수: 선형성을 가지는 대수로 이루어진 방정식들의 해를 구하는 방법론 혹은 학문
- 고유값(eigen value)와 고유벡터(eigen vector)에 대해 설명해주세요.  
정방행렬 A를 벡터 x에 곱했을 때 변환된 전과 후가 평행할 경우 x를 고유벡터라고 한다. 이 때 변환된 크기의 정도를 고유값이라고 한다.

- 리샘플링일란  
리샘플링은 내가 가지고 있는 샘플에서 다시 샘플 부분집합을 뽑아서 통계량의 변동성을 확인하는 것. 대표적인 예로 K-fold cross validation이 있음

## 머신러닝
- Cross Validation  
overfitting을 막기 위해서 데이터 세트를 여러 조합의 훈련 및 검증 세트로 나누어서 모델 학습과 평가를 수행하는 것. K-fold cross validation이 대표적임. Stratified k-fold는 불균형이 큰 경우에 사용하는 방법으로서 전체 데이터셋의 레이블이 지닌 분포를 반영하여 k-fold를 나누는 것임
- 성능 평가 metric: https://velog.io/@cgotjh/%EA%B8%B0%EC%B4%88-%EA%B3%B5%EB%B6%80
- 정규화와 표준화: feature들의 값의 범위를 비슷하게 만들어 줌으로써 더 robust한 feature extraction이 가능하게 함. 정규화는 X - Xmin / Xmax - Xmin을 통해서 값의 범위를 [0, 1] 사이로 옮김. outlier에 영향을 많이 받음. 표준화(z-score normalization)는 X - m / s을 통해 표준정규분포를 따르도록 함
- 차원의 저주  
데이터가 고차원이 될 수록 데이터가 지닌 configuration의 개수가 지수적으로 증가하면서 데이터 공간에 비해 데이터 표본의 수가 상대적으로 매우 적게 되는 현상. 이에 따라 ML model이 좋은 성능을 내도록 학습하기가 어려워짐. 차원 축소를 통해서 이를 해결해야 함
- 차원 축소  
  - feature selection: 특정 변수들만을 선택하여 사용. 해석이 용이하지만 변수간 상관관계가 고려되지 않음
  - feature extraction: 기존 변수들의 변환을 통해 새로운 변수를 추출함. 변수간 상관관계를 고려하여 변수의 개수를 많이 줄일 수 있음. 추출된 변수의 해석이 어려움. ex) PCA, wavelets transforms, autoencoder (unsupervised)
  - PCA: 주성분 추출을 통해 차원 축소를 수행하는 기법. 데이터를 축에 사영했을 때 가장 높은 분산을 가지는 데이터의 축을 찾아 그 축(주성분)으로 차원을 축소하는 것. 높은 분산을 갖는 축(주성분)을 찾는 이유는 정보의 손실을 최소화 하기 위함. 다른 의미에서 분산이 크다는 것은 그만큼 주성분이 원래 데이터의 분포를 잘 설명해줄 수 있음을 의미함
    - 추출된 변수 Z는 모든 기존 변수들의 선형결합으로 이루어짐. Z = alpha.T * X. Z의 분산을 최대화하는 alpha를 찾는 것이 PCA의 목적임
    - 고유값과 고유벡터: 특정 행렬 A에 대해 상수 lambda와 벡터 x가 다음 식을 만족할 때, lambda와 x를 각각 A의 고유값과 고유벡터라고 부름. Ax = lambda * x. 고유벡터는 선형변환 (행렬을 곱합)에 의해서 방향이 변하지 않는 벡터를 의미함

### 선형회귀모델
- 정의: 출력변수 Y를 입력변수 X들의 선형결합으로 표현한 모델. E(Y) = f(X). 입력값 X와 Y의 평균과의 관계를 구함
- 확률오차 가정: 오차항 e는 N(0, s^2)의 정규분포를 따른다. 이에 따라 Y는 N(f(x), s^2)의 정규분포를 따르게 됨
- 함수식의 파라미터를 추정하는 것이 우리의 목표임. loss function (L2 loss)을 각 파라미터에 대해 편미분을 하여 이 값이 0이 되는 파라미터 값들을 구함. 이를 최소제곱법이라고 함
- 또는 모델 학습시 gradient descent를 통해서 parameter 업데이트를 수행하기도 함

### 로지스틱 회귀모델
- Y 값이 연속형이 아니라 범주형인 경우, 즉 분류 문제의 경우 사용. X 변수의 선형결합식에 로지스틱 함수를 취한 형태(비선형결합)로 표현. 확률 값이 특정 기준 보다 크면 범주 1, 작으면 범주 0과 같은 식으로 최종 output 나옴
- 로지스틱 함수: input 값 (음의 무한대 ~ 양의 무한대)에 대해 단조증가 (혹은 단조감소) 함수. output 값의 범위는 0 ~ 1. 미분 결과를 원 함수식으로 표현 가능
- E(Y) = P(Y = 1|X = x) = 관축치 x의 범주가 1일 확률 = 1 / 1 + e^-(b0 + b1x)
- odds: 성공 확률이 p로 주어질 때, p / 1-p. log(odds) = b0 + b1x (선형식)
- odds ratio: 나머지 입력변수는 모두 고정시킨 상태에서 한 변수를 1 단위 증가시켰을 때 변화하는 odds (성공확률)의 비율
- 로지스틱 회귀모델 학습: Maximum Likelihood Estimation
  - bernouli 확률변수 y의 확률함수는 다음과 같이 계산됨. f(y) = p(x)^y * (1-p(x))^(1-y)
  - 여기에 log를 취하면 선형식들의 합으로 표현됨. 이 log likelihood function이 최대가 되는 parameter를 찾는 것이 학습의 과정임. 즉 이 식에 음수를 취한 것이 목적 함수가 됨
- Cross Entropy: 두 확률 분포 (p(x), q(x))의 차이로서 음의 log likelihood fuction의 기대값이라고 할 수 있음. 따라서 log likelihood function을 최대로 한다는 것은 cross entropy를 최소로 만드는 것과 같음

### 서포트 벡터 머신
- 분류를 위한 지도학습 모델의 한 종류로서 support vectors를 사용하여 결정 경계(Decision Boundary)을 정의하는 모델
- Support vectors: 결정 경계와 가장 가까이에 있는 가 클래스의 데이터 포인트
- margin: 결정 경계와 서포트 벡터 사이의 거리
- "최적의 결졍 경계는 마진을 최대화한다."
- SVM에서는 결정 경계를 정의하는게 결국 서포트 벡터이기 때문에 포인트 중에서 서포트 벡터만 잘 골라내면 나머지 쓸 데 없는 수많은 데이터 포인트들을 무시할 수 있다. 그래서 매우 빠르다.

```python
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear')

training_points = [[1, 2], [1, 5], [2, 2], [7, 5], [9, 4], [8, 2]]
labels = [1, 1, 1, 0, 0, 0]

classifier.fit(training_points, labels)
print(classifier.predict([[3,2]]))
```

- hard margin: outlier를 허용하지 않고 기준을 까다롭게 세운 형태. 서포트 벡터와 결정 경계 사이의 거리가 너무 가까울 수 있음. overfitting 문제가 발생할 가능성
- soft margin: outlier를 어느정도 margin 안에 포함되도록 기준을 잡은 형태. 거리가 더 멀어짐. underfitting 문제가 발생할 수 있음

```python
classifier = SVC(C = 0.01)
```

- C 값이 클수록 hard margin, 작을 수록 softmargin임. 기본값은 1. 최적값은 데이터에 따라 다름

### K Nearest Neighbors
- K개의 가장 근접한 data로부터 majority voting을 수행하여 분류 또는 예측 (이 때는 target들의 평균값을 예측값으로 output)을 수행
- Instance-based learning: 모델이 없이 관측치 (instance) 만을 이용하여 새로운 데이터에 대한 예측을 수행
- Memory-based learning: 모든 학습 데이터를 메모리에 저장한 후 이를 바탕으로 예측을 수행
- Lazy learning: 모델을 별도로 학습하지 않은 채 테스트 데이터가 들어올 때에만 작동함
- hyperparameter K
  - K가 매우 작을 경우 데이터의 지역적 특성을 지나치게 반영하여 overfitting의 위험이 있고, 매우 클 경우 너무 많은 개체가 포함되어서 오분류할 위험 (underfitting)이 있음
  - 일정 범위의 K 값들에 대해서 misclassification error (%)를 구하여서 최종 K 값을 결정
- hyperparameter measure distance
  - Euclidean Distance: 각 coordinate 값 간 차이의 제곱합의 제곱근. 두 관측치 사이의 직선거리
  - Manhattan Distance: 각 좌표축 방향으로만 이동할 경우에 계산되는 거리
  - Mahalanobis Distance: 변수 내 분산과 변수 간 공분산을 모두 반영한 거리. 데이터의 covariance matrix가 identity matrix인 경우에는 euclidean distance과 동일함. 해당 값의 제곱의 자취의 방정식을 그려보면 타원의 형태를 가짐


### K-Means Clustering
- 데이터 clustering (비슷한 속성의 데이터들을 묶음)을 위해 널리 사용되는 비지도학습 알고리즘
- Clustering이 사용되는 예: 추천 엔진, 검색 엔진, 시장 세분화 등
- 두 가지 질문: 몇 개의 그룹으로 나눌 것인가? / 데이터의 "유사도"를 어떻게 정의할 것인가?
- K: 데이터 set에서 찾을 것으로 예상되는 cluster 수
- Means: 각 데이터로부터 그것이 속한 cluster의 중심까지의 평균 거리. 이 값을 최소화하는 것이 알고리즘의 목표임
- 원리
    1. K개의 임의의 중심점(centroid)를 배치함
    2. 각 데이터들을 가장 가까운 중심점으로 할당하여 군집을 형성함
    3. 형성된 군집을 기준으로 해당 군집의 중심점을 업데이트 함
    4. 2와 3을 반복하여서 수렴될 때 까지 수행

```python
from sklearn.cluster import KMeans
model = KMeans(n_clusters=k)
model.fit(data)
model.predict(samples)
```

- K값, 군집의 개수 정하기

```python
print (model.inertia_)
```

- inertia 값은 각 데이터로부터 군집의 중심점까지의 거리로서 응집도를 의미함. inertia 값이 낮을 수록 군집화가 잘 된 것. K 값을 바꿔가면서 inertia 값의 변화를 확인
- 문제점
    - 처음에 중심점을 무작위로 설정하기 때문에 최적의 클러스터로 묶는 데 한계가 있음
    - 이를 해결하기 위해 K-Means++이 나옴
- K-Means++
    - 데이터 포인트 중 하나를 선택하여 중심점으로 지정
    - 두번째 중심점은 첫번째 것으로부터 최대한 먼 곳에 있는 데이터 포인트로 선정
    - 전통적인 K-means 보다 수렴하는 속도가 빠르다.

```python
from sklearn.cluster import KMeans
model = KMeans(n_clusters=k,  init='k-means++')
```

- 사실 init의 기본값이 'k-means++'임. 전통적인 k-means로 돌리려면 init='random'으로 해야함

### Decision Tree
- Tree 구조로 질문들을 구성하여 데이터를 분류하는 알고리즘. 일종의 스무고개
- Gini 불순도: 다른 클래스의 데이터가 포함된 정도
- Information Gain: 이전 단계의 불순도 - 다음 단계의 불순도
- Weighted Information Gain: 분할 후 생성된 데이터의 비율을 가중치로 정하고 불순도와 가중치를 곱해서 정보 획득량을 구함
- Information Gain이 큰 질문을 먼저 배치하는 것이 중요함. 이러한 과정을 재귀적으로 반복하면서 최적의 트리를 찾게됨

```python
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(training_points, training_labels)

predictions = classifier.predict(test_data)
print(classifier.score(test_data, test_labels))
```

- 한계점
    - 기본적으로 greedy 알고리즘을 토대로 작동하기 때문에 항상 최적의 해를 찾는 것은 아니다. 하지만 최적의 트리를 찾는 것은 어려운 일임
    - Tree가 커질 수록 overfitting 가능성이 생김. 이것을 제한하려면 가지 치기를 하거나DecisionTreeClassifier(max_depth = n)와 같이 트리의 최대 크기를 지정할 수도 있음
    

### Random Forest
- 훈련을 통해 구성해놓은 다수의 나무들로부터 분류 결과를 취합해서 결론을 얻는 일종의 인기투표와 같은 알고리즘. 다수의 알고리즘을 사용하는 앙상블 머신러닝 모델
- 다수의 나무를 기반으로 예측하기 때문에 overfitting의 가능성이 낮음
- Bagging: 전체 데이터 중 일부를 골라서 이를 기반으로 하나의 트리를 만듦. 이런 식으로 반복하여 다수의 트리를 형성 (데이터 중복 허용). 보통 전체 속성 개수의 제곱근만큼 선택하는게 일반적임. 이렇게 각 트리를 만들 때 속성들을 제한함으로써 각 나무들에 다양성을 부여함
```python
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 100)
# fit(), predict(), score()
```
