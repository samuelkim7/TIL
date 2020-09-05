### 멀티 프로그래밍
- 멀티 프로그래밍: CPU 활용도를 극대화하는 스케쥴링 알고리즘
- 프로세스 상태
  - running state: 실행 중. -> ready or block
  - ready state: 실행 대기 상태 -> running
  - block state: 특정 이벤트 발생 대기 상태. Wait (예: 파일 읽기, 프린팅). 끝나면 ready로 넘어감
  - Ready State Queue, Running State Queue, Block State Queue를 함께 사용하여 스케쥴링
<img src=https://user-images.githubusercontent.com/65876994/91558071-92fec300-e970-11ea-8069-52577e751541.PNG width=500 height=300>

### 선점형과 비선점형 스케쥴러
- 선점형 (Preemptive): 하나의 프로세스가 다른 프로세스를 대신해서 CPU를 차지할 수 있음. 기본적으로 최근의 운영체제들은 선점형 방식을 채택 
- 비선점형 (Non-preemptive): 한 프로세스가 끝나거나 block 상태가 되어야 다른 프로세스가 CPU를 사용할 수 있음. 응답시간이 길어질 수 있음

### 복합적 스케쥴링
- 예시1) 정적 우선순위 기반, 프로세스 상태 고려, 시분할 방식 (2초의 time quantum), 선점형 방식 (time quantum 이내 적용 또는 time quantum 시점에 적용)
- 최신의 알고리즘은 위의 예시 보다 훨씬 더 복잡한 방식임

### 인터럽트
- CPU가 프로그램을 실행 중일 때, 입출력 장치에서 이벤트가 발생하거나 예외상황이 발생할 경우 CPU에 알려서 처리하는 기술
- 주요 인터럽트
  - Divide-by-Zero Interrupt: 예외 상황 처리를 위한 인터럽트의 일종 -> 프로세스 중지
  - Timer Interrupt: 특정시점마다 인터럽트를 발생시킴. 선점형 스케쥴러를 위해 필요
  - 입출력 인터럽트: IO 처리 완료시 프로세스를 block -> ready 로 바꿔주는 인터럽트
- 인터럽트 종류
  - 내부: 프로그램 내부의 에러에 의해 발생 (0으로 나눔, 계산 결과 overflow 등). 소프트웨어 인터럽트
  - 외부: 주로 하드웨어에서 발생 (IO or Timer Interrupt). 하드웨어 인터럽트

### 시스템콜과 인터럽트
- 시스템콜 실행을 위해서는 코드에 인터럽트 명령을 넣어 CPU에게 실행시켜야 한다.
- 시스템콜 인터럽트 명령 호출 -> 커널 모드로 바뀜 -> 0x80에 해당하는 시스템콜 함수 실행 -> 다시 사용자 모드로 변경 -> 해당 프로세스의 다음 코드 진행
```shell
mov eax, 1 (시스템콜 번호)
mov ebx, 0 (인자)
int 0x80 (시스템콜 인터럽트 번호)
```
- IDT(Interrupt Descriptor Table): 인터럽트 번호에 해당하는 함수의 주소 기록. 인터럽트 발생시 IDT를 확인하여 해당 함수가 수행됨 (커널 모드)
