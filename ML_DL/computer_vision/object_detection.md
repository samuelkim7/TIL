### basic concepts
- Localization: 단 하나의 Object 위치를 Bounding box로 지정하여 찾음
- Object Detection: 여러 개의 Object들에 대한 위치를 Bonding box로 지정하여 찾음
- Segmentation: Detection보다 더 발전된 형태로 Pixel 레벨 Detection 수행
- Localization/Detection은 Object의 위치를 찾는 Bounding box regression(box의 좌표값을 예측)과 Object를 판별하는 Classification 두개의 문제가 합쳐져 있음

### 구성 요소
- 영역 추정 (Region Proposal): Object의 위치를 찾는 기법
- Deep Learning 네트워크 구성: Feature Extraction, Network Prediction
- 기타 요소: IOU, NMS, mAP, Anchor box

### 난제
- Classification + Regression을 동시에 해야함. 여러 물체를 판별하고 동시에 위치를 찾아야 함
  - 크기나 모양이 다양한 object가 섞여있는 이미지에서 이들을 detect 해야 함
  - object가 명확하지 않거나 중첩되어 있거나 차지하는 비중이 높지 않은 경우들이 있음
- detect 시간이 중요함. 실시간 영상 기반에서 detect해야하는 요구사항 증대
- 훈련 가능한 데이터 세트의 부족. annotation을 포함한 데이터 세트를 만드는 것이 어려움

### 영역 추정
#### Sliding Window 방식
- Window를 왼쪽 상단에서 부터 오른쪽 하단으로 이동시키면서 Object를 Detection하는 방식
- 다양한 형태의 window 사용 / window scale 고정 후 이미지 scale를 변경하는 방식
- Object Detection의 초기 기법. 수행 시간이 오래걸리고 검출 성능이 상대적으로 낮음

#### 영역 추정 기법
- "Object가 있을 만한 후보 영역을 찾자"
- Selective Search: segment들을 컬러, 무늬, 크기, 형태에 따라 grouping 수행 -> 이에 근거하여 bounding box를 만들고 region proposal 수행
  - 1차, 2차, 3차 거듭 진행되면서 점점 더 큰 segment group을 형성하고, 점점 더 큰 bounding box를 제시함
- IoU (Intersection over Union): 모델이 예측한 결과와 실측(Ground Truth) Box가 얼마나 정확하게 겹치는가를 나타내는 지표. 성능 평가를 위해 사용
  - IoU = 교집합의 크기 / 합집합의 크기
