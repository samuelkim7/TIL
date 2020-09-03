### 개념
- Light Weight Process 라고도 함
- 하나의 프로세스에 여러 개의 스레드 생성 가능. 함께 동시 실행 가능
- 한 프로세스 안에 있으므로, 프로세스의 데이터를 모두 접근 가능
- *프로세스 간에는 각 프로세스의 데이터 접근이 불가

### 특징
- 스택 영역 안에 각 스레드를 위한 스택 공간을 생성하여 실행됨 (각각의 PC, SP 가짐)
- 코드, 데이터, 힙 영역은 공유함 (주소영역도 공유하게 됨)

### 멀티 프로세싱과 Thread
- 멀티 프로세싱: 멀티 코어에서 병렬 처리를 통해 프로그램 실행 속도를 향상시킴
- 멀티 프로세싱은 Thread를 여러개 만들어서 구현할 수도 있음

### Thread의 장점
- 성능 향상. 사용자에 대한 응답성 향상
- 효율적인 자원 사용 (IPC 기법 사용하지 않고 메모리 자원 공유)
- 작업이 분리되어 코드가 간결해보임

### Thread의 단점
- 하나의 스레드만 문제가 있어도 전체 프로세스가 영향을 받음
- 스레드가 많아지면, context switching이 많이 일어나서 성능이 저하될 수 있음
  (리눅스 OS에서는 Thread를 Process와 같이 다룸. 스케쥴러를 통한 context switching에 의해 동시 실행)
  
### 동기화
- 작업들 사이의 실행 시기를 맞추는 것
- 동기화 이슈: 여러 스레드가 동일한 자원(데이터)에 접근하여 수정할 시 각 스레드의 결과가 영향을 받음

### 동기화 문제 예시
```python
import threading

g_count = 0

def thread_main():
  global g_count         # 전역변수를 사용하겠다고 선언
  for i in range(100000):
    g_count = g_count + 1

threads = []

for i in range(50):
  th = threading.Thread(target = thread_main) # 스레드 생성
  threads.append(th)

for th in threads:      # 스레드 실행
  th.start()

for th in threads:      # 동기화: 다른 스레드가 다 끝나도록 기다림
  th.join()
  
print('g_count = ', g_count)  # 모든 스레드가 끝난 뒤 마지막 코드 실행
```
**원래 결과 값은 5000000이 나와야 하지만, 실행시 마다 다른 결과가 나옴 - 동기화 이슈 때문에 발생**
- 100000의 연산을 수행하는 도중에 context switching이 일어나서, 스레드별로 연산과 전연변수 값 저장의 순서가 엉켜져서 덧셈 누락이 발생하기 때문 

#### 해결: mutual exclusion
- 한 스레드가 공유 변수를 갱신하는 동안 다른 스레드의 동시 접근을 막는 기법
- 아래에서는 문제가 되는 연산 부분에 이를 적용함
- 임계 영역: 동시 실행될 경우 동기화 문제를 낳는 코드 부분
- 임계 자원: 동시에 수정하면 안되는 공유 자원
```python
import threading

g_count = 0

def thread_main():
  global g_count         # 전역변수를 사용하겠다고 선언
  lock.acquire()         # 아래의 코드가 임계 영역임
  for i in range(100000):
    g_count = g_count + 1
  lock.release()

lock = threading.Lock()
threads = []

for i in range(50):
  th = threading.Thread(target = thread_main) # 스레드 생성
  threads.append(th)

for th in threads:      # 스레드 실행
  th.start()

for th in threads:      # 동기화: 다른 스레드가 다 끝나도록 기다림
  th.join()
  
print('g_count = ', g_count)  # 모든 스레드가 끝난 뒤 마지막 코드 실행
```

