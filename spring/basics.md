## 스프링 웹 기초

### 정적 컨텐츠
- static folder 안에 .html 파일 만들경우 스프링을 통해 localhost:8080/~.html 로 바로 접근 가능
- 먼저는 ~ controller를 찾고, 없을 경우 static folder 내의 html 파일을 찾아서 렌더링

### MVC 및 템플릿 엔진
- templates folder 안의 html 파일 (thymeleaf 엔진 사용)
- url에 해당하는 controller에서 model에 data를 담고 html 파일의 이름 반환 -> viewResolver가 templates/~.html로 변환하고 화면 이동 -> Thymeleaf 템플릿 엔진 처리 후 렌더링

### API 방식
- 
