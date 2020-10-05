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
- 컨트롤러
- 서비스: 핵심 비즈니스 로직 구현
- 리포지토리: 데이터베이스 접근, 도메인 객체를 DB에 저장하고 관리
- 도메인: 비즈니스 도메인 객체 ex) 회원, 주문, 쿠폰 등

### 테스트 케이스 작성
- JUnit 프레임워크 사용
- 
