### 기본 개념
- xml 방식: 의존성으로 사용하는 부품들의 결합 상태를 xml 설정 파일에 명시했음. 이런 경우 소스 코드를 변경하지 않고도 결합 상태를 수정할 수 있음
- Annotation 방식: 소스 코드 위에 바로 표시. 부품을 갈아끼우면 설정이 바로 적용됨 

### @Autowired
- 필요한 의존성을 IoC 컨테이너에서 찾아서 자동으로 injection 해달라는 의미
- spring을 통한 bean 객체 생성시 @Autowired 태그를 찾아서 자동으로 injection  
  (xml에서 설정시 <context:annotation-config /> 포함시켜주어야 생성된 bean 내의 annotation 검색)
- 기본적으로 타입을 기준으로 의존성 검색. 둘 이상인 경우 변수명을 기준으로 검색. @Qualifier로 검색할 bean의 name 설정 가능
- 태그 위치: 멤버변수 (기본 생성자 호출), overloaded 생성자 (@Qualifier를 parameter 앞에 씀), setter
- @Autowired(required = false): bean 객체가 없어도 error 없이 일단 실행되도록 함

### Annotation을 이용한 의존성 객체 생성
- @Component 태그 사용
- xml에 <context:component-scan base-package="" />를 포함시켜 주어야 함
- 이 경우 <context:annotation-config /> 는 없어져도 무방함
