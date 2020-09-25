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

### Filter and Interceptor
- Filter: 디스패처 서블릿의 앞 단에서 작동함. J2EE 표준 스펙에 있는 서블릿의 기능
- Interceptor: 디스패처 서블릿에서 컨트롤러로 가기 전에 동작. spring framework에서 제공. spring bean 사용 가능
