#!/usr/bin/env python
# coding: utf-8

# ### 1. 변수: 데이터를 저장하는 공간
# 저장공간(memory)에 값을 생성하고 이름(name)을 지정. = 를 사용.
# 
# *함수: 특정 기능을 반복적으로 호출하여 사용가능한 코드블럭
# 
# shift + tap : 함수에 대한 Docstring 제공
# 
# type() : 변수의 type을 return
# 
# c = None  ==> 초기화시 값을 정하지 않을 때 사용 (null과 같음)
# 
# a ** b = a^b
# 
# ### 2. 문자열
# '' 또는 ""로 생성
# ''' ''' 를 사용할 경우 문자열 내에 줄띄움 가능
# 
# ~~~python
# a = 'Hello World'
# print(a[10])      # d
# print(a[0:5])     # Hello
# 
# a.upper()            # HELLO WORLD
# a.replace('H', 'j')  # jello World
# ~~~

# In[4]:


# format 함수 : 문자열 내의 특정 값을 변수로부터 초기화하여 동적으로 문자열을 생성
temp = 25.5
prob = 80.0

a = '오늘 기온은 {}도 이고, 비올 확률은 {}% 입니다.' .format(temp, prob)
a


# In[2]:


# split 함수 : 특정한 문자 구분을 기준으로 문자열을 리스트로 치환
a = 'hello world. What a nice weather!'
a.split()


# ### 우선순위
# - NOT > AND > OR

# In[2]:


a = 10
b = 8
c = 11


# In[3]:


if a == 10 or b == 9 and c == 12:
    print('that is true')


# In[4]:


if (a == 10 or b == 9) and c == 12:
    print('that is true')


# ### if의 조건이 bool이 아닌 경우
# - False로 간주되는 값 (각 타입의 기본값)
#  - None, 0, 0.0, ''
#  - [], (), {}, set()
# - 그 밖에는 모두 True로 간주

# In[ ]:


# ! ~ 100까지 더하기
num = 1
_sum = 0

while num <= 100:
    _sum += num
    num += 1
    
print(_sum)


# In[1]:


# dict 순회하기
a = {'a':1, 'b':2, 'c':3}

for key in a:
    print(key, a[key])


# In[2]:


# tuple을 이용해서 key, value 출력
# items() : (key, value) 형태의 tuple들을 출력 
for key, value in a.items():
    print(key, value)


# #### range 함수
# - 리스트를 쉽게 만들게 하는 내장함수
# - 물론 리스트화 하려면 list(range(a))와 같이 써야함
# 
# ~~~python
# range(a)        # 0 ~ a-1까지의 리스트
# range(a, b)     # a ~ b-1까지의 리스트
# range(a, b, c)  # a ~ b-1까지를 c의 interval로 리스트화
# ~~~

# In[ ]:


# 구구단 출력
for i in range(2,10):
    for dan in range(1, 10):
        print(i, 'x', dan, '=', i*dan)

