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
- tf.Variable: mutable object. w, b 등의 learnable parameter. **ResourceVariable type**
- tf.constant: immutable object. dataset 등. **EagerTensor type**
- Variable -> constant 로 변환할 수 없음 (.convert_to_tensor()로는 변환 가능)
- constant -> Variable 로 변환 가능
- Variable + constant -> constant

```python
test_list = [1, 2, 3]
test_np = np.array([1, 2, 3])

t1 = tf.constant(test_list)
t2 = tf.constant(test_np)

print(t1)
print(t2)

print(type(t1))
print(type(t2))
```
