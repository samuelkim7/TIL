### list & tuple

list - mutable

tuple - immutable       ==> 요소의 값을 바꿀 수 없음

cf) string - **immutable**   

~~~python
a = 'Hello' 
a[0] = 'j'               # error
d = a.replace('H','j')   # 가능
print(a)                 # Hello
~~~


list : 다른 type의 변수도 함께 담을 수 있음


```python
# list() 함수 : 다른 데이터 타입을 리스트로 변환
a = 'hello world'
b = list(a)
print(b)
```

    ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    


```python
# list slicing
# start:end:increment(1)
a = [1,2,3,4,5,6,7,8]
print(a[3:5])
print(a[1:])
print(a[1:7:2])
```

    [4, 5]
    [2, 3, 4, 5, 6, 7, 8]
    [2, 4, 6]
    


```python
# list 멤버 함수
a = [1,2,3,4,5]
a.append(10)
print(a)

b = [6,7,8,9,10]

# a.extend(b)
a += b
print(a)

a.insert(0,40)
print(a)

a.remove(2)
print(a)

c= a.pop(2)      # 값이 없을 경우 마지막 것 지움. 값을 넣으면 인덱스로 지움. 반환값 있음
print(a)
print(c)
```

    [1, 2, 3, 4, 5, 10]
    [1, 2, 3, 4, 5, 10, 6, 7, 8, 9, 10]
    [40, 1, 2, 3, 4, 5, 10, 6, 7, 8, 9, 10]
    [40, 1, 3, 4, 5, 10, 6, 7, 8, 9, 10]
    [40, 1, 4, 5, 10, 6, 7, 8, 9, 10]
    3
    


```python
# in
a = [1,2,3,4,5,10]
b = 7

c = b in a  
print(c)

# 정렬
d = [3,7,1,3,7,0,293,62,6545,245,12,91]
d.sort()        #reverse=True 라고 할 경우 역정렬

print(d)

# sorted() : 정렬된 list를 반환. 원 정렬은 변하지 않음
```

    False
    [0, 1, 3, 3, 7, 7, 12, 62, 91, 245, 293, 6545]
    


```python
# Tuple unpacking : 값을 차례대로 변수에 대입
a, b, c= 100, 200, 300
print(a, b, c)
```

    100 200 300
    


```python
a = 5
b = 4
print(a,b)

a, b = b, a
print(a,b)
```

    5 4
    4 5
    


```python

```
