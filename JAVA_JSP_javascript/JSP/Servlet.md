### 웹 서버
- 이전에는 클라이언트와 서버 프로그램을 각각 만들고, 둘 간의 데이터 전송을 위해 socket, RPC 등을 사용 -> 전송 상의 문제, 클라이언트 프로그램의 업데이트 문제가 야기됨
- HTTP(웹)이 부상하면서 웹에 서버 클라이언트 프로그램을 올려서 사용하게됨
- 클라이언트의 페이지 요청에 대해 미리 만들어진 정적인 페이지를 전송하던 기존의 웹 방식 -> DB 연동을 통한 동적인 페이지 생성 및 전달 방식 구현
- 클라이언트는 동적으로 생성된 웹 문서만을 받아서 표시하기 때문에 웹브라우져만 있으면 됨 -> 웹개발자는 주로 서버 개발에만 집중하게 됨
- javascript의 등장으로 웹 프론트엔드 개발이 부상하게 됨

### Servlet의 개념
- "필요에 따라 사용될 수 있도록 각각 조각나 있는 Server Application"
- 항상 extends HttpServlet
- main 함수가 아닌 service 함수가 주 함수로 사용됨
- 톰캣은 사용자의 요청 URL과 mapping된 Servlet 코드를 찾아서 실행 (web.xml에 mapping 정보가 입력됨)
- 클라이언트의 입력을 받는 Request 객체와 클라이언트에게 출력을 보내는 Response 객체를 지님

### Servlet을 이클립스 없이 실행하기
- ~.java 형태로 Servlet을 작성한 후 javac -cp ...\servlet-api.jar ~.java 로 컴파일 (톰캣 lib 내의 jar file)
- 실행을 위해서는 톰캣이 찾을 수 있도록 예약된 위치에 두어야 함 ( ...\TomcatProject\WEB-INF\classes\ )
- web.xml에 mapping 정보 입력 후 톰캣 실행 (startup.bat)
- url 접근

*TomcatProject 폴더 내의 파일은 사용자가 요청할 수 있지만, 그 하위 WEB-INF 폴더 내의 파일은 사용자가 직접 요청할 수 없고 mapping 정보에 의한 접근만 가능함

### Eclipse IDE에서 Servlet 사용
- Eclipse workspace\해당project\webcontents : 홈디렉토리와 같은 역할을 함
- webcontents 내의 파일 실행: Tomcat의 webapps 디렉토리로 파일이 배포된 후 실행됨
- Eclipse 내의 window\web browser\Default system browser : 기본 브라우져를 통해 실행되도록 설정
- Servlet 파일 생성: Project\Java Resources\src 내에 class file 생성
- web.xml에 mapping 정보 입력 (project 생성시 web module이 2.5버전 정도여야 web.xml 파일이 생성됨, 없을 경우 복사해와서 사용해도 무방)

### Servlet 출력 형식 지정
- 서버에서 보낼 때 인코딩 방식 지정 (한글이 깨지지 않도록 2byte 씩 데이터를 전송하게 됨): response.setCharacterEncoding("UTF-8")
- 브라우져가 읽는 type 형식 지정: response.setContentType("text/html; charset=UTF-8") -> response Headers에 type이 포함되어서 전송됨

### Annotation을 이용한 mapping
- Servlet 3.0부터 가능해짐. web.xml에서 

### Get 요청
- 클라이언트가 어떤 웹 문서를 달라고 요청하는 것. 요청시 추가적인 옵션을 붙이는 것이 Query String임
- Servlet에서는 입력 도구인 request를 이용하여 query string을 읽어들일 수 있음 (항상 문자열로 읽힘)

#### query string에 값이 없거나 null인 경우 처리 
```java
void service(){
String cnt_ = request.getParameter("cnt");   // 임시 변수에 저장

int cnt = 100;                               // 기본값 설정
if(cnt_ != null && !cnt_.equals(""))         // null이 아니고 ""도 아니라면
  cnt = Integer.parseInt(cnt_);
  
for(int i=0; i<cnt; i++){
  out.print("Hello");
}
}
```

### Post 요청
- 입력할 내용이 많은 경우에 사용
