### Logback
- Log4j에 기반한 스프링 부트의 기본 로깅 프로그램
- Log4j에 비해 성능은 10배 정도 향상되고, 로그 설정 변경 후에도 서버에 바로 반영됨
- 로깅 구현체로 slf4j를 사용
- 콘솔, 파일, DB 등에 로그 기록 가능
- 먼저 logback-spring.xml 파일 작성 후 사용하고자 하는 클래스에서 아래와 같이 입력
```java
private Logger log = LoggerFactory.getLogger(this.getClass());

log.debug("log content");
```

- lombok을 사용할 경우 @Slf4j 사용하면 로거를 생성할 필요가 없음
```java
@Slf4j
public class ...

log.debug("log content");
```

### log4jdbc
- 로그에 출력되는 sql 쿼리, 관련 정보를 정렬된 상태로 출력해줌

### Interceptor
- 클라이언트의 url 요청시 컨트롤러의 처리 전 후에 특정한 작업을 수행하기 위해 사용
- Interceptor: 디스패처 서블릿에서 컨트롤러로 가기 전에 동작. spring framework에서 제공. spring bean 사용 가능
- cf) Filter: 디스패처 서블릿의 앞 단에서 작동함. J2EE 표준 스펙에 있는 서블릿의 기능
- HandlerInterceptorAdapter 클래스를 상속받아서 구현
  - preHandle: 컨트롤러 수행 전에 수행
  - postHandle: 컨트롤러 수행 후 결과를 뷰로 보내기 전에 수행
  - afterCompletion: 뷰 작업까지 완료된 후 수행
- 그런 다음 WebMvcConfigurer를 상속받는 클래스에서 Interceptor 등록
```java
@Configuration
public class WebMvcConfiguration implements WebMvcConfigurer{
	
	@Override
	public void addInterceptors(InterceptorRegistry registry){
		registry.addInterceptor(new LoggerInterceptor());
	}
}
```
-ex) 각 요청의 시작과 끝을 보여 주는 로그 출력 구현 ( preHandle, postHandle에 로그 log.debug(); 삽입)
```java
@Slf4j
public class LoggerInterceptor extends HandlerInterceptorAdapter {
	
	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception{
		log.debug("======================================          START         ======================================");
		log.debug(" Request URI \t:  " + request.getRequestURI());
		return super.preHandle(request, response, handler);
	}
	
	@Override
	public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
		log.debug("======================================           END          ======================================\n");
	}
}
```
