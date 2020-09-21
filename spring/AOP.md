### Aspect Oriented Programming
- 사용자 관점의 주 업무 로직(Core Concern)에 더해지는 다른 관점 (개발자, 운영자)의 보조적인 업무와 관련된 로직을 따로 분리해내서 구현하는 방식 (Cross-cutting Concern)  
  (예시: 로그 처리, 보안 처리, 트랜잭션 처리)
- "반복되는 흩어진 코드들을 따로 한 곳으로 모아서 구현"
- Proxy를 통해서 Core Concern 앞뒤에 코드를 삽입한 것과 같은 실행 흐름을 만듦
- Spring을 이용하면 AOP를 구현하기가 쉬움
- 3가지 구현 방법
  - 컴파일  A.java --(AOP)--> A.class (AspectJ)
  - 바이트코드 조작 A.java -> A.class --(AOP)--> 메모리 (AspectJ)
  - 프록시 패턴 (스프링 AOP) [참고](https://refactoring.guru/design-patterns/proxy)  
     : 프록시를 구현하여 기존 코드를 변경하지 않고 새로운 기능을 추가

### AOP 적용 예제
- java로 구현
```java
public static void main(String[] args) {
	Exam exam = new NewlecExam(1,1,1,1);

	Exam proxy = (Exam) Proxy.newProxyInstance(NewlecExam.class.getClassLoader(),
		new Class[] {Exam.class},
		new InvocationHandler() {
					
			@Override
			public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
				long start = System.currentTimeMillis();

				Object result = method.invoke(exam, args);

				long end = System.currentTimeMillis();
				String message = (end - start) + "ms 시간이 걸렸습니다.";
				System.out.println(message);

				return result;
			}
		}
	);	
System.out.printf("total is %d\n", proxy.total());
System.out.printf("avg is %f\n", proxy.avg());
}
```
- spring으로 구현
```java
// @LogExecutionTime이라는 annotation이 있는 method를 joinPoint로 받음
// 해당 메서드의 앞뒤로 시간을 측정하고 log로 남기는 코드를 삽입

@Component
@Aspect
public class LogAspect {

	Logger logger = LoggerFactory.getLogger(LogAspect.class);

	@Around("@annotation(LogExecutionTime)")
	public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
		StopWatch stopWatch = new StopWatch();
		stopWatch.start();

		Object proceed = joinPoint.proceed();

		stopWatch.stop();
		logger.info(stopWatch.prettyPrint());

		return proceed;
	}
}
```
