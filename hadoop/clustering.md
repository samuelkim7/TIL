## VirtualBox 설치
https://www.virtualbox.org/wiki/Downloads
- 현 사용 버전: 6.1.12
-설치 파일 실행하여 VirtualBox 설치함

## centOS7 설치
https://www.centos.org/download/ 
- 7버전 x86_64 -> mirror선택
- CentOS-7-x86_64-DVD-2003.iso 다운

#### VirtualBox에서 VM 만들기
- New 클릭
- Linux / Red Hat 선택 (64-bit)
- Memory 2GB -> create a virtual hard disk now -> Fixed size -> 20GB -> Create
- 생성된 VM 더블클릭 -> CentOS7 이미지 파일 선택 -> start

#### CentOS7 설치
- Software Selection -> Base Environment: Infrastructure Server
- Installation Destination -> 표시된 디스크 선택 (자동 파티션 설정됨) -> Done
- Begin Installation
- Root Password 설정
- 설치 끝난 후 Reboot
- 라이선스 약관 동의
- root 계정으로 로그인

*설치 관련 참고 링크*
- https://jyoondev.tistory.com/32?category=824268 : virtual box 관련된 부분
- https://lsjsj92.tistory.com/134?category=762556 : centOS7 자체 설치 관련 부분                                                                                  
                                                            

## 자바 설치
```shell
# 기존 패키지 확인
rpm -qa | grep java

# 기존 패키지 삭제
yum remove package명
```

- 윈도우에서 jdk-1.8.0...tar.gz 다운로드 후 WinSCP로 리눅스로 옮김
```shell
tar xfvz jdk…tar.gz

mv jdk… /usr/local

# 심볼릭 링크 설정
ln -s jdk… java 

# 환경 변수 등록
vi /etc/profile

# 맨 하단에 아래의 내용 추가 후 저장 (i + 수정 후 ESC + :wq + Enter)
export JAVA_HOME=/usr/local/java
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH="."

# 설정 적용
$ source /etc/profile

# 설치 및 설정 확인
$ java -version
```

*참고 링크*
https://jg-seo.tistory.com/3

## 클러스터링
- 리눅스 서버 종료. VirtualBox 내에서 해당 서버 우클릭 후 복제
- hadoop02로 명명. MAC 주소 정책: 새 MAC 주소 생성 선택
- 복제 방식: 완전한 복제 선택
- hadoop03, hadoop04도 동일한 방식으로 생성 (총 4개의 서버)
- 각 서버 우클릭 -> 설정 -> 네트워크 -> 어댑터에 브리지 선택
- 각 서버 실행 -> root 계정 접속

- 방화벽 끄기
```shell
systemctl stop firewalld
systemctl disable firewalld
firewall-cmd --state ==> 꺼졌는지 확인
```

- host name 지정
```shell
vi /etc/hostname

# 각각의 서버에서 hadoop01, hadoop02, hadoop03, hadoop04로 변경 후 저장
```

- ip주소 고정 (GNOME 데스크탑)
  - 각 서버의 GNOME 데스크탑 -> applications -> system tool -> settings -> network
  - Wired의 설정 버튼 클릭
  - IPv4 -> Manual 선택 -> 고정할 IP 입력 ex) 192.168.1.32 ~ 35 (서버 4대)
  - Netmask, Gateway, DNS 서버 입력 (브라어져 상에서 게이트웨이로 접속하여 확인)
  - 만약 다른 사용자들이 있다면 내가 정한 IP 주소와 겹치지 않도록 게이트웨이 -> 내부 네트워크 설정 에서 동적 IP 주소 범위를 설정해줌
  - reboot -> IP주소 잘 설정되었는지 확인 (ifconfig or ip addr)

- ip주소 고정2 (nmtui)
  - netmask는 기본 255.255.255.0으로 잡힘
  - automatically activate 체크 (space bar)

- 클러스터링할 서버 네트워크 정보 추가
```shell
$ vi /etc/hosts

#기존 내용은 지우고 아래와 같이 변경 (서버 4대 모두)
127.0.0.1        localhost
192.168.1.32     hadoop01
192.168.1.33     hadoop02
192.168.1.34     hadoop03
192.168.1.35     hadoop04
```
- reboot

- ssh 접속 설정
- ssh 공개키/비밀키 한쌍을 생성하고 공개키를 각 서버에 저장하면 비밀번호 없이 ssh 접속 가능 (방화벽이 꺼져있어야만 가능)
```shell
ssh-keygen -t rsa (Enter 3번)

# 접속할 서버의 authorized_keys 파일에 공개키 추가
ssh-copy-id root@hadoop02

# 이렇게 각 서버에서 자신을 포함한 4개의 서버에 대해 공개키 추가해줌 (16번)
# ssh 접속 확인 (hadoop01에서)
ssh root@hadoop02 # 암호를 묻지 않고 접속된다면 잘 설정된 것임
```
*참고 링크*
- https://jg-seo.tistory.com/3

## 하둡 설치
- hadoop01(master)에 설치 후 나머지 서버에 배포하는 방식

#### 하둡 다운로드
- https://archive.apache.org/dist/hadoop/core/
-해당 설정에서는 hadoop-2.7.2.tar.gz 다운 -> WinSCP로 옮김
``` shell
tar xfvz hadoop-2.7.2.tar.gz
mv hadoop… /usr/local

# 심볼릭 링크 생성
ln -s hadoop… hadoop
```

#### 환경 변수 설정 (https://jg-seo.tistory.com/3와 동일하게 설정)
```shell 
vi /etc/profile # 해당 링크와 동일하게 설정

# 위 링크 내용에 아래 내용 추가
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop

cd /usr/local/hadoop/etc/hadoop
```
- hadoop-env.sh 수정 (JAVA_HOME만 추가하기)
- slaves 파일 수정
- core-site.xml 수정
- mkdir /usr/local/hadoop/tmp (core-site.xml 설정과 맞추기 위해 디렉토리 생성)
- hdfs-site.xml 수정 (replication value는 2로 해도 됨)
- cp mapred-site.xml.template mapred-site.xml
- mapred-site.xml 수정 (spark를 사용할 예정인 경우 설정하지 않아도 됨)
- yarn-site.xml 수정 (아래 내용에 따라)
```shell
<property>
	<name>yarn.nodemanager.aux-services</name>
	<value>mapreduce_shuffle</value>
</property>
<property>
	<name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
	<value>org.apache.hadoop.mapred.ShuffleHandler</value>
</property>
<property>
	<name>yarn.resourcemanager.resource-tracker.address</name>
	<value>hadoop01:8031</value>
</property>
<property>
	<name>yarn.resourcemanager.scheduler.address</name>
	<value>hadoop01:8030</value>
</property>
<property>
	<name>yarn.resourcemanager.address</name>
	<value>hadoop01:8032</value>
</property>
<property>
	<name>yarn.resourcemanager.webapp.address</name>
	<value>hadoop01:8088</value>
</property>
<property>
	<name>yarn.nodemanager.pmem-check-enabled</name>
	<value>false</value>
</property>
<property>
	<name>yarn.nodemanager.vmem-check-enabled</name>
	<value>false</value>
</property>
```

-마지막 두 설정이 들어가야만 memory 사용량 초과시 yarn 작업이 자동으로 꺼지는 것을 막을 수 있음
$ source /etc/profile

*참고 링크*
- spark만 사용할 경우 위 링크와 함께 https://m.blog.naver.com/PostView.nhn?blogId=superbag2010&logNo=220791657218&proxyReferer=https:%2F%2Fwww.google.com%2F 참고

- slave들에게 하둡 디렉토리 배포
```shell
scp -r hadoop-2.6.5 root@hadoop02:/usr/local
scp -r hadoop-2.6.5 root@hadoop03:/usr/local
scp -r hadoop-2.6.5 root@hadoop04:/usr/local

# slave 서버들에서도 하둡 심볼릭 링크 생성
ln -s /usr/local/hadoop-2.6.5 hadoop

# profile 전송
scp /etc/profile root@hadoop02:/etc/profile
scp /etc/profile root@hadoop03:/etc/profile
scp /etc/profile root@hadoop04:/etc/profile

# slave 서버들에서도 각각 설정 적용
source /etc/profile

# 자바 및 하둡 설치 확인
java -version
hadoop version
```

## hadoop 실행
```shell
# hadoop01에서 포맷 진행
hadoop namenode -format

# 실행 ($HADOOP_HOME/sbin 으로 이동한 후)
start-dfs.sh
start-yarn.sh

# 하둡 프로세스 확인 (jvm 위에서 돌아가는 프로세스 확인 명령어)
jps
```

## 오류 발생시
- 실행중 일단 stop-all.sh 로 작동을 멈추고 jps 로 프로세스가 켜져있는지 확인 후 켜져있을 경우 프로세스 킬
- 그리고 모든서버에서 logs 폴더안에 있는 log를 띄운다음 다시 start-all.sh 을 이용하여 켜준다음 에러 로그를 파악
- 로그 확인 방법
$ tail -10000f [log 파일명]

## 스파크 설치 on YARN
-hadoop01에서 스파크 다운 (Spark 2.3.2 Pre-build for hadoop 2.7)
```shell
tar xfvz spark…

# /usr/local 위치로 옮긴다음 심볼릭 링크 생성

# 환경변수 설정
vi /etc/profile
export SPARK_HOME=/usr/local/spark
export PATH=$PATH:$SPARK_HOME/bin

source /etc/profile

#slave들에 profile 배포 후 
source /etc/profile

# hadoop 구동 없는 상태, hadoop01에서 spark 홈으로 이동
spark-shell # scala shell 나오는 것 확인

# spark on yarn 실행 예시
cd spark
$ spark-submit --class org.apache.spark.examples.SparkPi \
--master yarn \
--deploy-mode client \
--driver-memory 1g \        (==default 값)
--executor-memory 1g \    (==default 값)
--executor-cores 1 \          (==default 값)
/usr/local/spark/examples/jars/spark-examples*.jar \
10

# default configuration 설정 (선택 사항)
cd spark/conf/spark-defaults.conf
```

## jupyter notebook 설치
```shell
yum install -y python3

wget …

python3.6 get-pip.py

pip3 install jupyter notebook
```
