### 1. 변수: 데이터를 저장하는 공간
저장공간(memory)에 값을 생성하고 이름(name)을 지정. = 를 사용.

*함수: 특정 기능을 반복적으로 호출하여 사용가능한 코드블럭

shift + tap : 함수에 대한 Docstring 제공

type() : 변수의 type을 return

c = None  ==> 초기화시 값을 정하지 않을 때 사용 (null과 같음)

a ** b = a^b

### 2. 문자열
'' 또는 ""로 생성
''' ''' 를 사용할 경우 문자열 내에 줄띄움 가능

~~~python
a = 'Hello World'
print(a[10])      # d
print(a[0:5])     # Hello

a.upper()            # HELLO WORLD
a.replace('H', 'j')  # jello World
~~~


```python
# format 함수 : 문자열 내의 특정 값을 변수로부터 초기화하여 동적으로 문자열을 생성
temp = 25.5
prob = 80.0

a = '오늘 기온은 {}도 이고, 비올 확률은 {}% 입니다.' .format(temp, prob)
a
```




    '오늘 기온은 25.5도 이고, 비올 확률은 80.0% 입니다.'




```python
# split 함수 : 특정한 문자 구분을 기준으로 문자열을 리스트로 치환
a = 'hello world. What a nice weather!'
a.split()
```




    ['hello', 'world.', 'What', 'a', 'nice', 'weather!']


