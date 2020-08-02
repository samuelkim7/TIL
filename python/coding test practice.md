### [백준] 사칙연산
공백으로 분리된 입력을 받아서 사칙연산 수행 후 출력


```python
a, b = map(int, input().split())

print(a+b, a-b, a*b, a//b, a%b, sep='\n')
```

    5 10
    15
    -5
    50
    0
    5
    

### [백준] A+B-8
특정한 형식으로 출력하기


```python
cases = int(input())

for i in range(1, cases+1):
    a, b = map(int, input().split())
    print("Case #%s: %s + %s = %s" %(i,a,b,a+b))
```

    5
    1 2
    Case #1: 1 + 2 = 3
    3 4
    Case #2: 3 + 4 = 7
    5 7
    Case #3: 5 + 7 = 12
    2 43
    Case #4: 2 + 43 = 45
    3 5
    Case #5: 3 + 5 = 8
    

### 테스트 케이스가 없는 경우에 대한 처리
try / except 사용


```python
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
```

    
    


```python
#ord() : 헤당 문자의 아스키 코드 출력
a = input()
print(ord(a))
```

    A
    65
    

### [백준] 알파벳 찾기
주어진 문자열에 대해 각 알파벳이 나온 첫번째 index를 출력


```python
Str = input()
ans = [-1] * 26
for i in range(len(Str)):
    if ans[ord(Str[i])-ord('a')] != -1:       #이미 값이 있는 할당된 경우 continue
        continue
    else:
        ans[ord(Str[i])-ord('a')] = i         #해당 문자의 인덱스를 ans 리스트의 요소로 할당

for i in ans:
    print(i, end=' ')
```

    baekjoon
    1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 


```python
cases = int(input())

for i in range(cases):
    n, str = input().split()
    for s in str:
        print(int(n)*s, end='')
    print()
```

    2
    5 aa
    aaaaaaaaaa
    3 abc
    aaabbbccc
    


```python
Str = input().upper()
cnt = [0]*26
for i in range(len(Str)):
    cnt[ord(str[i])-65] += 1
max_num = max(count)
print(max_num)
if cnt.count(max_num) >= 2:
    print('?')
else:
    print(chr(cnt.index(max_num) + ord('A')))
print(ord('A'))
```

### [백준] 숫자의 개수
자연수 A,B,C에 대해 AXBXC의 값에서 0부터 9까지의 숫자가 몇 번씩 쓰였는지 출력


```python
#풀이1 : count list 이용. O(n)
multiplied = 1
for i in range(3):
    n = int(input())
    multiplied *= n

count = [0]*10
for s in str(multiplied):
    count[int(s)] += 1

for i in count:
    print(i)
```


```python
#풀이2 : str.count() 함수 사용. O(n^2). 하지만 여기서는 개수가 정해져있으므로 빠르게 수행됨
mult = int(input()) * int(input()) * int(input())
for i in range(10):
    print(str(mult).count(str(i)))
```
