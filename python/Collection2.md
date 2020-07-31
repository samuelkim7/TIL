### dictionary
- 키:값 형태로 요소 저장
- hashMap과 같음
- 순서를 따지지 않음. 즉, 인덱스가 없음
- 사용빈도 높음

### set
- dictionary에서 key만 활용하는 데이터 구조로 이해
- 중복 허용 X, 순서 없음
- 수학에서 집합의 개념과 동일


```python
# update() : 두 개의 dict를 병합

a = {'a':1, 'b':2, 'c':3}
b = {'a':2, 'd':4, 'e':5}

a.update(b)

print(a)
```

    {'a': 2, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    


```python
# del 키워드 / pop() 함수

a = {'a':1, 'b':2, 'c':3}
print(a)

a.pop('b')
print(a)

del a['c']
print(a)
```

    {'a': 1, 'b': 2, 'c': 3}
    {'a': 1, 'c': 3}
    {'a': 1}
    


```python
# clear()
a = {'a':1, 'b':2, 'c':3}
print(a)
a.clear()
print(a)
```

    {'a': 1, 'b': 2, 'c': 3}
    {}
    


```python
# in
a = {'a':1, 'b':2, 'c':3}
print(a)

b = [1,2,3,4,5,6,9,10,100]

print(100 in b)      # O(n)
print('b' in a)      # O(1)
```

    {'a': 1, 'b': 2, 'c': 3}
    True
    True
    


```python
# get() ==> 키 값이 없을 경우 none을 반환
print(a.get('d'))

#print(a['d'] ==> 키 값이 없을 경우 에러
```

    None
    


```python
# 모든 keys, values 접근
print(a)
print(list(a.keys()))
print(list(a.values()))

list(a.items())     # key, value 형태의 tuple들을 반환
```

    {'a': 1, 'b': 2, 'c': 3}
    ['a', 'b', 'c']
    [1, 2, 3]
    




    [('a', 1), ('b', 2), ('c', 3)]




```python
#set 선언
a = {1,2,3,4,5,6,7}

#빈 set 생성
b = set()
```


```python
# list -> set
a = [1,2,3,3,3,4,56,67,78]
print(a)
b = set(a)
print(b)
```

    [1, 2, 3, 3, 3, 4, 56, 67, 78]
    {1, 2, 3, 4, 67, 78, 56}
    


```python
# set에서 수학의 연산 수행
a = {1,2,3}
b = {2,3,4}

print(a.union(b))  # 합집합
print(a.intersection(b))  # 교집합
print(a.difference(b))  # 차집합
print(a.issubset(b))  # 부분집합?
```

    {1, 2, 3, 4}
    {2, 3}
    {1}
    False
    
