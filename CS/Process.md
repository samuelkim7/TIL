### 멀티 프로그래밍
- 멀티 프로그래밍: CPU 활용도를 극대화하는 스케쥴링 알고리즘
- 프로세스 상태
  - running state: 실행 중. -> ready or block
  - ready state: 실행 대기 상태 -> running
  - block state: 특정 이벤트 발생 대기 상태. Wait (예: 파일 읽기, 프린팅). 끝나면 ready로 넘어감
  - Ready State Queue, Running State Queue, Block State Queue를 함께 사용하여 스케쥴링
