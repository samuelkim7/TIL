*하둡 완벽 가이드 4판 - 톰 화이트*

## 하둡과 맵리듀스
### 배경 및 역사
- 현재는 빅데이터가 곳곳에서 생산되는 시대임
- 디스크의 용량은 커졌으나 (1TB 정도) 전송 속도는 100MB/s 수준임 -> 디스크 전체를 읽는데 약 2.5시간이 걸림
- 해결책: 여러 개의 디스크에서 동시에 데이터를 읽는 것
  - 문제1: 많은 하드웨어를 사용하는 만큼 장애 가능성도 증가함. 이를 대비하여 데이터를 여러 디스크에 복제해야함
  - 문제2: 분석을 위해서는 분할된 데이터들을 하나로 결합해야함. 맵리듀스가 이를 해결
- 2003년 발표된 구글의 GFS, 2004년 발표된 구글의 맵리듀스에 착안한 너치 분산 파일시스템으로 시작
- 2006년 하둡이라는 이름의 프로젝트로 분리되어 나와서 야후팀과 합류한 후, 야후에서 2008년 하둡 클러스터 구현 및 발표

### 특징
- 데이터를 클러스터에 분할하여 저장하고, 맵과 리듀스 함수를 사용해 분리된 파티션들에서 병렬로 데이터를 처리함
- 전체 데이터셋을 대상으로 일괄 분석이 가능함. 대화형 분석에는 적합하지 않음
- 한번 쓰고 여러번 읽는 애플리케이션에 적합함
- 텍스트나 이미지와 같은 비정형 데이터도 잘 처리함. schema-on-read
- 정규화를 수행하지 않음. 매번 모든 데이터를 완전하게 표시함
- 분산 컴퓨팅 시 실패한 프로세스를 자동으로 감지하여 장애가 없는 머신에 재배치하도록 구현됨
- cf) RDBMS: 지속적으로 변경되는 데이터셋에 적합함. 정형화된 데이터를 다룸. 중복 제거와 무결성을 위해 정규화가 필요

### 분산 컴퓨팅에 대비한 멀티 프로세싱의 문제점
1) 일 분산의 문제: 파일별 크기가 다를 경우 결국 가장 긴 파일을 처리하는 프로세스의 처리 시간에 의해 전체 수행 시간이 결정됨. 이를 위한 대안은 전체 파일을 일정 단위의 데이터 청크로 나누고 각 청크를 하나의 프로세스에 할당하는 것
2) 결과 통합의 문제: 개별 프로세스의 모든 결과를 합친 다음 이에 대한 처리를 다시 수행해야함
3) 단일 머신의 처리 능력 한계

### 맵리듀스 기본
- 맵 단계와 리듀스 단계는 둘 다 입력과 출력으로 키-값의 쌍을 사용한다. (데이터 타입은 선택)
- 예시: 기상 센서의 로그 데이터로부터 연도별 최고 기온 구하기
  - 맵 함수의 입력: (file offset, 문자열 형태의 로그 데이터)
  - 맵 함수의 출력: (연도, 기온) -> 키를 기준으로 정렬 및 그룹화
  - 리듀스 함수의 입력: (연도, [기온1, 기온2, ...])
  - 리듀스 함수의 출력: (연도, 최고 기온)
  - 구성: Mapper class, Reducer class, Mapreduce Job class
- 일반적으로 전체 데이터를 128MB의 스플릿으로 분리하여 병렬 처리함
- 맵 태스크의 결과는 로컬 디스크에 저장되고, 맵리듀스 잡이 완료된 후 맵의 결과는 버려진다. 리듀스의 결과는 안정성을 위해 HDFS에 저장됨
- 리듀스 태스크의 수는 독립적으로 지정 가능. 이 수는 잡의 실행 시간에 영향을 크게 미치므로 튜닝이 필요함 
- 다수의 리듀스 태스크가 존재하는 경우: 리듀스 태스크의 수 많큼 파티션이 생성되며 각 파티션에 맵의 결과가 분배됨 ('셔플')
- 컴바이너 함수: 맵 함수의 결과를 그룹화하여 리듀스 함수의 입력으로 보냄

## HDFS
### 특징
- 높은 데이터 처리량(TB~PB)을 위해 최적화되어 있고 응답 시간은 희생됨
- 따라서 빠른 응답 시간을 요구하는 application은 HDFS와 맞지 않음
- 단일 writer로 파일을 한번 씀. 파일의 끝에 덧붙이는 것은 가능하지만 임의 위치에 있는 내용을 수정할 수는 없음
- 데이터 무결성
  - 모든 데이터를 쓰는 과정에서 내부적으로 체크섬을 계산하고, 읽는 과정에서 기본적으로 체크섬을 검증함
  - cf) *checksum: A checksum is a sequence of numbers and letters used to check data for errors. If you know the checksum of an original file, you can use a checksum utility to confirm your copy is identical.*
  - 만약 클라이언트가 블록을 읽는 과정에서 체크섬에러를 검출하면 이를 네임노드에 보고함 -> 네임노드는 해당 블록의 정상 복제본을 다른 데이터노드에 복제하여 복제 계수를 원래 수준으로 복구하고 손상된 복제본을 삭제함

### 블록
- hdfs 파일은 블록으로 나누어지며 각 블록은 독립적으로 저장된다.
- 기본적인 블록의 크기는 128MB이며, 블록의 크기 보다 작은 데이터의 경우 데이터의 크기만큼만 디스크를 사용한다.
- 이렇게 큰 블록을 사용하는 이유는 블록의 시작점을 탐색하는 데 걸리는 시간을 줄이기 위함이다.
- 또 다른 블록의 이점은 스토리지의 서브시스템을 단순하게 만들 수 있다는 것과 내고장성과 가용성을 위한 복제(보통 3개)를 구현하기에 매우 적합하다는 점이다.

### 네임노드와 데이터노드
- 네임노드: 파일시스템 트리, 트리 안의 모든 파일, 디렉토리에 대한 메타데이터 유지 / 파일에 속한 모든 블록이 어느 데이터노드에 있는지 파악 (시스템 시작시 새롭게 받아와서 메모리에서 관리)
- 데이터노드: 클라이언트나 네임노드의 요청이 있을 때 블록을 저장하고 탐색함. 저장 중인 블록의 목록을 주기적으로 네임노드에 보고
- 네임노드의 장애복구 기능 구현
  1) 파일시스템의 메타데이터를 백업
  2) 보조 네임노드 운영: 네임 스페이스 이미지의 복제본 보관 (시간차 존재)
- 블록 캐싱: 빈번하게 접근하는 블록 파일은 데이터노드의 메모리에 캐싱하여 보관 -> 읽기 성능 향상
- 페더레이션: 네임노드를 추가하여 네임스페이스를 나누어 저장하게 함

## YARN
- 하둡 2에서 처음 도입된 클러스터 자원 관리 시스템. 사용자가 직접 접근하지는 않는다.
- 클러스터의 계산 계층에 해당하며, YARN 위에서 분산 컴퓨팅 프레임워크가 실행된다.
- 구성
  - 리소스 매니저: 클러스터 전체 자원의 사용량을 관리
  - 노드 매니저: 특정 애플리케이션 프로세스가 실행되는 컨테이너를 구동하고 모니터링함 (태스크 트래거와 동일)
- cf) 맵리듀스1 
  - 잡트래커: 태스크 스케쥴링을 통해 모든 잡을 조율함. 태스크 실패시 다른 태스크 트래커에 해당 태스크를 맡김
  - 태스크 트래커: 태스크를 실행하고 진행 상황을 잡트래커에 전송
- 맵리듀스1에 대비한 YARN의 이점
  1) 확장성: 리소스 매니저에 더하여 맴리듀스 잡 당 하나의 애플리케이션 마스터를 둠으로써 2.5배 정도의 노드와 태스크까지 관리 가능
  2) 가용성: 마찬가지로 애플리케이션 마스터가 추가되어서 각 애플리케이션의 가용성이 증가됨
  3) 다중 사용자: 맵리듀스 뿐만이 아니라 다양한 분산 애플리케이션 수용 가능
