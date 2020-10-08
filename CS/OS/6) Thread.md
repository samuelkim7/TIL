## Thread 기초
### 기본 개념
- 프로세스 내에서 동작하는 여러 실행의 흐름. Light Weight Process 라고도 함
- 하나의 프로세스에 여러 개의 스레드 생성 가능. 함께 동시 실행 가능
- 한 프로세스 안에 있으므로, 프로세스의 데이터를 모두 접근 가능
- *프로세스 간에는 각 프로세스의 데이터 접근이 불가*

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
  
## 동기화
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
  global g_count            # 전역변수를 사용하겠다고 선언
  lock.acquire()            # 임계 영역에 들어갈 수 있도록 lock을 요청함
  for i in range(100000):
    g_count = g_count + 1
  lock.release()            # 임계 영역에서 나온 후 lock을 해제함

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

### Mutex와 세마포어
- Mutex: 임계구역에 하나의 스레드만 들어갈 수 있음
- Semaphore: 임계구역에 여러 스레가 들어갈 수 있음
  - P: 검사 (임계영역에 들어갈 때). S값이 1 이상이면 임계 영역 진입 후 S 값 1 차감 (S == 0 이면 대기. 대기 하는 동안 loop를 수행)
  - V: 증가 (임계영역에서 나올 때). S값을 1 더하고 임계 영역에서 나옴
  - S: 세마포어 값 (이 수 만큼의 프로세스가 동시에 접근 가능)
  - 바쁜 대기: 임계영역에 들어가기를 대기하는 동안 반복문을 계속 수행하는 상태 -> CPU 성능 저하 야기
  - 대기큐: 대기 상태일 경우 바쁜 대기 대신 대기큐에 넣어서 loop를 돌지 않도록 만들어줌
  - wakeup(): S가 1이상이 되면 대기큐에 있는 프로세스를 재실행
  
### 교착상태와 기아상태
- 교착상태 (Deadlock): 두 개 이상의 작업이 서로가 끝나기만을 기다리는 무한 대기 상태. 여러 프로세스가 동일 자원 점유를 요청할 때 발생
  - 네가지 조건(상호배제, 점유대기, 비선점, 순환대기)이 모두 만족할 때 교착상태 발생 가능성이 있음 (**참고**)  
  - 해결: 위의 네 조건 중 한 두가지 조건을 제외시켜야 함
  - 예시: Thread1 - 자원 a를 locking한 상태에서 자원 b의 lock을 요청 / Thread 2 - 자원 b를 locking한 상태에서 자원 a의 lock을 요청  
           -> 둘 다 요청 자원의 lock을 얻지 못하고 무한히 대기하게 됨
- 기아상태 (Starvation): 특정 프로세스의 우선순위가 낮아서 원하는 자원을 계속 할당 받지 못하는 상태
  - 여러 프로세스가 부족한 자원을 점유하기 위해 경쟁할 때, 특정 프로세스는 영원히 자원 할당을 받지 못하는 경우
  - 해결: 1)프로세스 우선순위를 수시로 변경 2)오래 기다린 프로세스의 우선순위 높여주기 3)요청 순서대로 처리하는 FIFO 기반 요청큐 사용
