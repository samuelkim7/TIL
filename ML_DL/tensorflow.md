### anaconda 가상환경 설정
```python
conda create -n [name] python=3.x       # 생성
conda remove -n [name]                  # 제거
conda activate [name]                   # 활성화
conda deactivate                        # 나가기
pip install [package]                   # 활성화된 상태에서 패키지 설치
conda install spyder                    # 가상환경 내에 spyder 설치
spyder                                  # 가상환경 내에서 spyder 실행
```

### 변수
- tf.Variable: mutable. w, b 등. ResourceVariable type
- tf.constant: immutable. dataset 등. EagerTensor type
