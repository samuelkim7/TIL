## 운영체제(OS)의 역할
1. 시스템 자원 관리자
- 시스템 자원 (하드웨어): CPU, Memory, I/O devices, 저장매체
- CPU나 memory가 어떻게 배분되어 사용될지, 저장매체 내 어디에 저장될지 등은 하드웨어 스스로 결정할 수 없고 운영체제가 필요하다.

2. 사용자와 컴퓨터 간의 커뮤니케이션 지원
3. 컴퓨터 하드웨어 및 프로그램을 제어
- 응용 프로그램의 관리 및 실행을 담당 -> 응용 프로그램이 효율적으로 동작하도록 지원

## 운영체제와 응용 프로그램 (Application)의 관계
- 소프트웨어: 운영체제 / 응용 프로그램 (한글, 엑셀 등등)
- 운영체제: 응용 프로그램이 요청하는 시스템 자원을 효율적으로 분배하고 지원하는 소프트웨어
- 운영체제는 응용 프로그램의 권환 관리, 실행, 종료를 담당함
- 응용 프로그램: 운영체제 위에서 실행되는 소프트웨어

### cf) 운영체제의 실행
- 운영체제는 하드디스크에 설치 및 저장된다.
- 컴퓨터가 켜질 때 운영체제는 메모리에 올라가서 실행된다.
- 참고: 폰노이만 구조

## 운영체제의 역사

### 1950년대
1. ENIAC
- 첫 번째 컴퓨터
- 운영체제가 없음. 하나의 응용 프로그램 실행하기도 바쁨
- 응용 프로그램이 시스템 자원을 제어

### 1960년대 초기
1. 배치 처리 시스템 (batch processing system) 도입
- 여러 응용 프로그램을 등록해두면 순차적으로 실행하는 시스템
- 단점: 컴퓨터 응답 시간이 오래 걸릴 수 있음. 실행 시간도 오래 걸릴 수 있음 (CPU가 필요 없음에도 프로그램이 CPU를 점유할 수 있음)
- 이를 기반으로 운영체제가 출현하게 됨

### 1960년대 후반
1. 시분할 시스템(Time Sharing System) 제안 (구현X)
- 응용 프로그램이 CPU를 사용하는 시간을 잘게 쪼개서, 여러 프로그램을 동시에 실행하는 기법
- 컴퓨터 응답 시간 최소화하여 다중 사용자를 지원하는 것이 목적
2. 멀티 태스킹 (Multi Tasking) 제안 (구현X)
- 단일 CPU에서 여러 응용 프로그램의 병렬 실행을 가능케 하는 기법
- 가능한 CPU를 많이 활용하도록 하는 것이 목적
- 전체 응용 프로그램의 실행 시간도 줄일 수 있음 (멀티 프로그래밍)
- 시분할 시스템과 유사한 기술 사용

### 1970년대
1. UNIX OS 탄생
- 현대 운영체제의 기본기술을 포함한 최초의 운영체제 (멀티 태스킹, 시분할 시스템, 멀티 프로그래밍 -> 다중 사용자 지원)
- 미국 AT&T 벨 연구소 (켄 톰슨, 데니스 리치)에서 개발됨
- C 언어가 먼저 개발된 후 C언어를 사용하여 UNIX가 개발됨
- 이전에는 Assembly 언어로 소프트웨어가 개발됨 (CPU 명령어 사용, memory 주소 지정) -> 컴퓨터마다 설정이 다르고 복잡도가 높음 -> 반면 C언어로 개발된 소프트웨어는 컴파일러에 의해 실행되기 때문에 컴퓨터 별 설정이 필요없음

### 1980년대
1. 개인용 컴퓨터 시대
- 이전에는 대형 컴퓨터에 여러명이 접속해서 사용 (UNIX)
- CLI -> GUI 로의 변화 (최초: apple 사의 Macintosh)
- CLI (Command Line Interface): 터미널 환경. 키보드로 커맨드 입력
- GUI (Graphical User Interface): GUI 환경. 마우스 클릭 기반

### 1990년대
1. 응용 프로그램의 시대
- 개인용 컴퓨터 사용자의 급증, Windows OS 대중화
- 엑셀, 워드 프로세서 등이 개발됨
2. 네트워크 기술의 발전
- WWW 인터넷 대중화
3. LINUX의 개발
- 오픈 소스, 무료
- 이뿐만 아니라 각종 오픈 소스 운동이 활성화됨

### 2000년대 이후
1. 오픈 소스 활성화
- Apache 웹서버, LINUX, MySQL, Android 등등
2. 가상머신, 대용량 병렬 처리 기술 등장

### 핵심 정리
1. 운영체제는 응용 프로그램과 시스템 자원을 제어하고 관리한다.
2. 응용 프로그램(Application)은 운영체제 위에서 실행되는 소프트웨어이다.
3. 배치 처리 시스템, 시분할 시스템, 멀티 태스킹, CLI/GUI의 개념