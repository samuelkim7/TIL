## 운영체제
- 운영체제의 역할
- 시스템 콜
- 프로세스 스케쥴링: 배치 처리 시스템/ 시분할 시스템/ 멀티 태스킹/ 멀티 프로그래밍
- 스케쥴러: FIFO/ SJF/ Priority-Based/ Round Robin
- 인터럽트
- 프로세스
  - 프로세스의 구조 및 실행
  - 컨텍스트 스위칭
  - IPC
- 스레드
  - 스레드의 개념 및 장단점
  - 멀티 프로세스 대신 멀티 스레드를 사용하는 이유
  - 스레드의 동기화 문제
  - Mutex와 세마포어
  - 교착상태(Deadlock)와 기아상태
- 가상 메모리
  - 작동 방식
  - 페이징 시스템
  - 페이지 폴트와 인터럽트
- 파일 시스템
  - inode 방식
- 부팅
- 가상 머신
<br><br><br>

### 운영체제의 역할
1. 시스템 자원 (CPU, Memory, I/O devices, 저장매체) 관리자: memory의 배분, 저장매체의 저장경로 지정, driver를 통한 입출력 장치 제어 등을 담당
2. 사용자와 컴퓨터 간의 커뮤니케이션을 위한 인터페이스 제공
3. 응용 프로그램의 권환 관리, 실행, 종료를 담당하며 응용 프로그램이 요청하는 시스템 자원을 분배함  
<a href="#top">TOP</a>

### 시스템 콜
- 운영체제 커널 영역의 각 기능을 호출하는 명령 또는 함수. 이를 통해 응용 프로그램은 운영체제와 상호작용하여 시스템 자원을 할당받음
- 응용 프로그램은 시스템콜을 각 언어별로 정리한 라이브러리인 API를 통해 시스템콜을 요청함
- ex) 응용 프로그램에서 특정 파일의 데이터를 읽는 기능을 구현하고 실행한다면, 해당 응용 프로그램이 사용하는 언어의 API를 통해서 시스템콜이 요청되고, 시스템콜이 커널 영역의 하드디스크에 있는 해당 파일을 열어서 그 데이터를 응용 프로그램에 전달한다.
- cf) 커널 모드: OS가 사용하는 CPU 권환 모드로서 메모리나 하드디스크와 같은 핵심 자원에 접근 가능
- cf) 사용자 모드: 응용 프로그램이 사용하는 CPU 권환 모드로 핵심 자원에 접근할 수 없음  
<a href="#top">TOP</a>

### 프로세스 스케쥴링
- 배치 처리 시스템: 자동으로 여러 응용 프로그램이 순차적으로 실행될 수 있도록 하는 시스템 (FIFO 형태). 응답 시간이 길어질 수 있으며, 둘 이상의 프로그램의 동시 실행 불가능
- 시분할 시스템 / 멀티 태스킹: 응용 프로그램의 CPU 점유 시간을 잘게 쪼개어 실행될 수 있도록 하여 응답 시간을 최소화 및 다중 사용자 지원. 단일 CPU에서 여러 응용 프로그램이 동시에 실행되는 것처럼 구현
- 멀티 프로그래밍: 특정 응용 프로그램이 CPU를 사용하지 않는 유휴시간 동안 다른 응용 프로그램에게 CPU를 할당하여 시간 대비 CPU 활용을 최대화함. Ready State Queue, Running State Queue, Block State Queue를 함께 사용하여 스케쥴링
- 멀티 프로세싱: 여러 CPU에 하나의 프로그램을 병렬로 실행하여 실행속도를 극대화함  
<a href="#top">TOP</a>

### 스케쥴러
- 정의: 특정 순서대로 프로세스가 실행되도록 관리함
- FIFO 스케쥴러: 배치 처리 시스템과 유사. 실행시간이 긴 프로세스가 먼저 도달하면 효율성이 떨어짐
- 최단 작업 (SJF, Shortest Job First) 스케쥴러: 실행시간이 짧은 프로세스 먼저 실행. 실행시간이 긴 프로세스는 CPU를 할당받는 것이 불가능해질 수 있음. 실행시간을 모두 알아야 구현 가능
- 우선 순위 기반 (Priority-Based) 스케쥴러 
  - 정적 우선순위: 프로세스 마다 미리 지정 / 동적 우선순위: 스케쥴러가 상황에 따라 우선순위를 변경
  - 선점형 스케쥴링 방식: 더 높은 우선순위의 프로세스가 도착하면 실행중인 프로세스를 멈추고 CPU 대신 차지 (최근에 주로 사용)
  - 비선점형 스케쥴링 방식: 더 높은 우선순위의 프로세스가 도착하면 Ready Queue의 Head에 넣고, 현 프로세스가 끝나거나 block 상태가 되면 다음 프로세스 실행
  - 문제점: 우선순위가 낮은 프로세스의 경우 무기한 blocking 상태에 빠질 수 있음
- Round Robin 스케쥴러
  - time quantum 만큼 실행 후 해당 프로세스를 ready queue의 마지막으로 보내는 방식 (시분할 기법). 현대적인 CPU 스케쥴링
  - 장점: response time이 빨라짐
  - 주의할 점: time quantum이 너무 커지면 FCFS와 같아짐. 너무 작을 경우 잦은 context switch로 overhead가 발생할 수 있음  
<a href="#top">TOP</a>

### 인터럽트
- CPU가 프로그램을 실행 중일 때, 입출력 장치에서 이벤트가 발생하거나 예외상황이 발생할 경우 CPU에 알려서 처리하는 기술
- 스프트웨어 인터럽트  
  - 프로그램 내부의 에러에 의해 발생 -> 프로세스 중지 (0으로 나눔, 계산 결과 overflow 등)
- 하드웨어 인터럽트
  - Timer Interrupt: 특정시점마다 인터럽트를 발생시킴. 선점형 스케쥴러를 위해 필요
  - 입출력 인터럽트: IO 처리 완료시 프로세스를 block -> ready 로 바꿔주는 인터럽트
- 시스템 콜과 인터럽트: 프로그램 실행 중 시스템콜 인터럽트 명령 호출됨 -> (커널 모드) 0x80에 해당하는 시스템콜 함수 실행 -> (사용자 모드) 해당 프로세스의 다음 코드 진행  
<a href="#top">TOP</a>
  
### 프로세스
- 프로세스의 구조 및 실행
- 컨텍스트 스위칭
- IPC  
<a href="#top">TOP</a>
  
### 스레드
- 스레드의 개념 및 장단점
- 멀티 프로세스 대신 멀티 스레드를 사용하는 이유
- 스레드의 동기화 문제
- Mutex와 세마포어
- 교착상태(Deadlock)와 기아상태  
<a href="#top">TOP</a>
  
### 가상 메모리
  - 작동 방식
  - 페이징 시스템
  - 페이지 폴트와 인터럽트  
<a href="#top">TOP</a>
  
### 파일 시스템
  - inode 방식  
<a href="#top">TOP</a>
  
### 부팅  
<a href="#top">TOP</a>

### 가상 머신  
<a href="#top">TOP</a>