### dataset
- 실제 올림픽 데이터를 참조하여 만들어진 sample dataset
- csv file (각 칼럼은 tap으로 구분됨)
- 칼럼 정보: 선수명, 나이, 나라, 연도, 폐회일자, 종목, 금, 은, 동, 총 메달

### hive
- 하둡 완전 분산 모드에 하이브 (1.2.2) 설치 완료
- 해당 dataset을 /root/hive 디렉토리에 저장
- 하둡 실행 후 hive 실행


#### 테이블 생성
hive> create table olympic (athelete STRING, age INT, country STRING, year STRING, closing STRING, sport STRING, gold INT, silver INT, bronze INT, total INT)  
        row format delimited  
        fields terminated by ‘\t’  
        stored as textfile;

#### 데이터 로딩
hive> load data local inpath ‘/root/hive/olympic_data.csv’ into table olympic;


#### 쿼리 수행
- 각각의 쿼리문의 실행 결과를 별도의 테이블로 저장
- 저장된 테이블을 hdfs dashboard에서 다운 받아서 정리
