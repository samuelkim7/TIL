### 개념
- 리눅스 컨테이너를 기반으로 하여 특정한 서비스를 패키징하고 배포하는데 유용한 오픈소스 프로그램
- Dockerfile --build--> Docker Image --run--> Docker Container 상에서 서버 실행
- Immutable Infrastructure: 서버를 구축한 이후에는 변경이나 업데이트를 할 수 없도록 하는 것. 업데이트가 필요할 경우 그냥 제거하고 새로운 이미지를 사용함
  - Immutable -> Stateless, Scalable
- VM과 Container의 차이점
  - VM: Host OS 위에 Guest OS를 올려서 거의 의존적이지 않은 별도의 컴퓨터와 같이 사용. 새로운 OS로 존재해야하기 때문에 용량도 크고 IO 기능들은 Host OS에 의존하기 때문에 성능도 느림 점이 있음
  - Container: Guest OS 없이 도커 엔진 위에서 동작함. 성능적으로도 개선된 편이며 메모리 용량도 적게 차지함. Host OS에 대한 의존성이 존재함. 200MB 전후의 경량 컨테이너로도 배포 가능
- 리눅스 컨테이너: 리눅스 상에서 격리된 여러 개의 시스템을 동작시키기 위한 가상화 기술
