## 스프링 웹 기초

### 정적 컨텐츠
- static folder 안에 .html 파일 만들경우 스프링을 통해 localhost:8080/~.html 로 바로 접근 가능
- 먼저는 ~ controller를 찾고, 없을 경우 static folder 내의 html 파일을 찾아서 보여줌

### MVC 및 템플릿 엔진
- templates folder 안의 html 파일 (thymeleaf 엔진 사용)
- url에 해당하는 controller에서 model에 data를 담고 html 파일의 이름 반환 -> **viewResolver**가 templates/~.html로 변환하고 화면 이동 -> Thymeleaf 템플릿 엔진 처리 후 렌더링

### API 방식
- @ResponseBody annotation 사용 (HTTP의 BODY에 문자 내용을 직접 반환)
- HttpMessageConverter가 동작
  - 문자열 처리: StringHttpMessageConverter
  - 객체 처리: MappingJackson2HttpMessageConverter가 객체를 JSON 방식으로 반환함
  
### 웹 애플리케이션 계층 구조
- 컨트롤러: 클라이언트의 요청을 받아서 처리함
- 서비스: 핵심 비즈니스 로직 구현
- 리포지토리: 데이터베이스 접근, 도메인 객체를 DB에 저장하고 관리
- 도메인: 비즈니스 도메인 객체 ex) 회원, 주문, 쿠폰 등

### 테스트 케이스 작성
- JUnit 프레임워크 사용
- @AfterEach를 통해 각 메서드 실행 후 repository를 클리어해줘야 함

### 스프링 빈 등록
- 두 가지 방식
  1) 컴포넌트 스캔을 통한 자동 의존관계 설정( @Component, @Controller, @Service, @Repository )
    - @SpringBootApplication이 있는 클래스의 패키지와 하위패키지들이 스캔의 범위임
  2) 자바 설정 클래스를 통해 직접 스프링 빈 등록
    - @Configuration 클래스에서 @Bean으로 등록
- 기본적으로 싱글톤으로 빈을 등록함
- DI에는 필드 주입, setter 주입 (의존관계 변경될 여지 O), 생성자 주입 3가지가 있지만 의존관계가 실행 중에 동적으로 변하는 경우는 없으므로 생성자 주입을 권장함
- 실무에서는 정형화된 컨트롤러, 서비스, 리포지토리는 컴포넌트 스캔을 사용. 상황에 따라 구현 클래스를 변경해야 하면 설정을 통해 스프링 빈으로 등록함z

### 스프링의 다형성 지원
- 개방, 폐쇄 원칙 (OCP): 확장에는 열려있고, 수정에는 닫혀있다.
- 스프링의 DI를 사용하면 **기존 코드를 전혀 손대지 않고, 설정만으로 구현 클래스를 변경**할 수 있다.

### 스프링 통합 테스트
- 스프링 컨테이너와 DB 연결을 포함한 테스트
- @SpringBootTest: 스프링 컨테이너와 테스트를 함께 실행한다.
- @Transactional: 테스트 케이스에 이 애노테이션이 있으면, 테스트 시작 전에 트랜잭션을 시작하고, 테스트 완료 후에 항상 롤백한다. 이렇게 하면 DB에 데이터가 남지 않으므로 다음 테스트에 향을 주지 않는다.

