### Aspect Oriented Programming
- "반복되는 흩어진 코드들을 한 곳으로 모아서 구현"
- 3가지 구현 방법
  - 컴파일  A.java --(AOP)--> A.class (AspectJ)
  - 바이트코드 조작 A.java -> A.class --(AOP)--> 메모리 (AspectJ)
  - 프록시 패턴 (스프링 AOP) [참고](https://refactoring.guru/design-patterns/proxy)
  
### 프록시 패턴
- 프록시를 구현하여 기존 코드를 변경하지 않고 새로운 기능을 추가함


### AOP 적용 예제
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
