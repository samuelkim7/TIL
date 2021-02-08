## RCNN
### Intro
- Object를 찾는 기법: Sliding Window 방식과 Region Proposal 방식이 있었음
- Region Proposal의 대표적인 방식이 Selective Search임. Segmentation 후 이것들을 합쳐가면서 Object가 있을 region을 추천함
- 마지막에 Softmax를 사용하지 않고 SVM classifier를 사용함. 이것이 Detection 성능을 올려주는 것이 확인되었기 때문에
- 먼저 Softmax로 학습시킨 후에 이 layer를 제거하고 SVM으로 대치하여 적용
- 전체적인 flow: Selective search -> Image crop과 Warp (model의 input size에 맞도록) -> CNN pretrained model 적용 -> SVM classifier로 분류 / Bounding Box Regression

### 장단점
- 다른 알고리즘 대비 매우 높은 Detection 정확도 -> Deep Learning과 Region Proposal 기반 Object Detection의 성능 입증
- 너무 느린 Detection 시간과 복잡한 아키텍처 및 학습 프로세스
  - 하나의 이미지 마다 selective를 수행하여 2000개의 region 이미지를 도출하고 이들을 각각 CNN feature map을 생성함으로 매우 느림
  - 한 장의 Object Detection을 하는데 약 50초 소요
  - Detection 수행 시간을 줄이고 복잡하게 분리된 아키텍처를 통합할 수 있는 연구를 수행하게 됨

## SPP (Spatial pyramid pooling) Net
- RCNN 개선 방안: 원본 이미지만으로 CNN Feature Map 생성한 후 원본 이미지의 Selective Search로 추천된 Region proposal 이미지를 Feature Map에 통과시킴
- 서로 다른 크기의 Region proposal 이미지 개선 방안: Feature Map을 통과한 후 SPP Net을 통해 고정된 크기의 Vector로 변환하여 FC에 input 제공


## Fast RCNN
- SPP를 ROI Pooling Layer로 바꿈. 7x7로 모두 바꿔줌
- SVM을 Softmax로 변환 -> End-to-End Network Learning 가능
- Classification과 Regression을 함께 최적화 (Multi-task loss 함수)
- Training Time, mAP, test time 모두 향상됨

