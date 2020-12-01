### basics
#### map() function
- map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
- Syntax: map(fun, iter)
  
Ex)
```python
numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result))
```
Output:
```python
[2, 4, 6, 8]
```

#### print() function
- parameters: sep, end 

#### == and is
==(equals) : comparing the values of the two variables 
is : checking if the two variables point to the same object

### Sequence types
- sequence is the generic term for an ordered set. List, tuple, range, str, bytes, bytearray are sequence types.
- Lists are the most versatile sequence type. The elements of a list can be any object, and lists are mutable they can be changed. Elements can be reassigned or removed, and new elements can be inserted.
- Tuples are like lists, but they are **immutable - they can't be changed.**
- Strings are a special type of sequence that can only store characters, and they have a special notation. However, all of the sequence operations described below can also be used on strings. Strings are **immutable.**
- sequence operations: +, \*, [i], slicing (+ and \* cannot be applied on range object)
- functions for sequence: len(), min(), max(), sum(), seq.index(x), seq.count(x), reversed()
- tuples and strings and ranges are immutable. So reassigning values cannot be done on them.

### if, while문
#### FizzBuzz
```python
for i in range(1, 101):
  print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
```

### list
- 할당: 새로운 객체가 생성되지 않음
```python
a = [1, 2, 3]
b = a
```
- 복사: 새로운 객체를 생성
```python
a = [1, 2, 3]
b = a.copy()

print(a is b)  # False
print(a == b)  # True
```

#### list comprehension
- Syntax: a = [식 for 변수 in 리스트 [if 조건문]]
```python
a, b = map(int, input().split())
c = [2**i for i in range(a, b+1)]
print(c)
```
Output:
```python
[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
```

#### map()
```python
x = input().split()  # 반환값: 문자열 리스트
m = map(int, x)      # 리스트의 요소를 int로 변환. 반환값은 map 객체 (iterator)
a, b = m             # unpacking을 통해 변수 여러개에 값을 
```
