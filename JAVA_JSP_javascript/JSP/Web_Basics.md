### 웹 서버의 발달
- 이전에는 클라이언트와 서버 프로그램을 각각 만들고, 둘 간의 데이터 전송을 위해 socket, RPC 등을 사용 -> 전송 상의 문제, 클라이언트 프로그램의 업데이트 문제 등이 야기됨
- HTTP(웹)이 부상하면서 웹에 서버 클라이언트 프로그램을 올려서 사용하게됨
- 클라이언트의 페이지 요청에 대해 미리 만들어진 정적인 페이지를 전송하던 기존의 웹 방식 -> DB 연동 등을 통한 동적인 페이지 생성 및 전달 방식 구현
- 클라이언트는 동적으로 생성된 웹 문서만을 받아서 표시하기 때문에 웹브라우져만 있으면 됨 -> 웹개발자는 주로 서버 개발에만 집중하게 됨
- 그 이후 javascript의 등장으로 웹 프론트엔드 개발이 부상하게 됨

### 웹 브라우저와 웹 서버
- URL (Uniform Resource Locator): 웹 상의 모든 자원에 대한 주소를 가리킴. protocol, 서버 이름, 경로로 구성됨
- 웹의 기본적인 통신 과정: 웹브라우저가 웹 서버에 URL 요청 -> 웹 서버는 웹 브라우저에 웹 페이지(HTML 문서) 제공 -> 웹 브라우저가 HTML 표준에 따라 화면 렌더링
- WAS (Web Application Server): 웹을 위한 연결, 데이터 베이스 연동 등과 같은 어플리케이션 구현을 위한 기능을 제공하는 웹 서버 
- JSP: 동적인 웹 페이지를 작성하기위한 자바의 표준 기술
- cf) hypertext: 새로운 웹 문서로 연결되는 text

### HTTP
- HTTP (HyperText Transfer Protocol): 웹 상에서 HTML, image, video, XML 등 다양한 데이터를 주고받을 때 사용하는 규칙
- HTTP request
  - 첫째줄: HTTP method, Path(query string 포함), HTTP version
  - Headers: 서버가 참조할 수 있는 정보 포함
  - (Optional) Body: POST와 같은 요청의 경우 여기에 data를 담음
- HTTP response
  - 첫째줄: HTTP version, status code, status msg
  - Headers: 응답의 길이, type 등의 정보를 포함
  - (Optional) Body: 요청된 자원 포함 (HTML 문서, image 등)
- [HTTP - MDN 문서](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
