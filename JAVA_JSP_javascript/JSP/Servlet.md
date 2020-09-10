### Servlet의 개념
- "필요에 따라 사용될 수 있도록 각각 조각나 있는 Server Application"
- 항상 extends HttpServlet
- main 함수가 아닌 service 함수가 주 함수로 사용됨
- 톰캣은 사용자의 요청 URL과 mapping된 Servlet 코드를 찾아서 실행 (web.xml에 mapping 정보가 입력됨)
- 클라이언트의 입력을 받는 Request 객체와 클라이언트에게 출력을 보내는 Response 객체를 지님

#### Servlet을 이클립스 없이 실행하기
- ~.java 형태로 Servlet을 작성한 후 javac -cp ...\servlet-api.jar ~.java 로 컴파일 (톰캣 lib 내의 jar file)
- 실행을 위해서는 톰캣이 찾을 수 있도록 예약된 위치에 두어야 함 ( ...\TomcatProject\WEB-INF\classes\ )
- web.xml에 mapping 정보 입력 후 톰캣 실행 (startup.bat)
- url 접근

*TomcatProject 폴더 내의 파일은 사용자가 요청할 수 있지만, 그 하위 WEB-INF 폴더 내의 파일은 사용자가 직접 요청할 수 없고 mapping 정보에 의한 접근만 가능함
