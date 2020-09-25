### Aspect Oriented Programming
#### 개념
- 사용자 관점의 주 업무 로직(Core Concern)에 더해지는 다른 관점 (개발자, 운영자)의 보조적인 업무와 관련된 로직(Cross-cutting Concern)을 따로 분리해내서 구현하는 방식     
  (로그 , 권한 체크, 인증, 예외 처리, 트랜잭션 처리 등에서 사용)
- 업무 로직의 시작이나 종료 시점에 반복적으로 사용되는 부가 기능을 한 곳에서 코드로 구현하기 위함
- cf) 기존의 OOP에서는 공통 기능 코드를 구현한 후 해당 기능이 필요한 모든 부분에서 클래스를 생성하고 메서드를 호출해야만 했음
- AOP를 적용하면 비즈니스 로직에서 공통 기능 코드를 직접 호출하지 않음. 컴파일이나 실행 시점에 공통 기능 코드가 삽입됨. 기존 로직의 변화 없이 원하는 시점에 코드를 삽입할 수 있음
- Aspect: 공통적으로 적용될 기능을 의미함. 한 개 이상의 Pointcut과 Advice의 조합으로 만들어짐
- Advice: Aspect의 구현체로 Joinpoint에 삽입되어 동작함 (동작 시점에 따라 Before, After, Around로 나뉨)
- Joinpoint: Advice를 적용하는 지점
- Pointcut: Advice를 적용할 Joinpoint를 선별하는 기준을 정의 (execution, within, bean 명시자 등)
- Target: Advice를 받을 대상
- Weaving: Advice를 적용하는 것. 즉 공통 코드를 원하는 대상에 삽입하는 것

#### 구현
- AspectJ를 통해서 구현하기도 했으나 현재는 Proxy를 이용해서 주로 구현
- Spring을 이용하면 AOP를 구현하기가 쉬움
- 프록시 패턴 (스프링 AOP) [참고](https://refactoring.guru/design-patterns/proxy)    
  - Proxy를 통해서 Core Concern 앞 뒤에 코드를 삽입한 것과 같은 실행 흐름을 만듦
  - 기존 코드를 변경하지 않고 새로운 기능을 추가 가능

### 적용 예제
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
- spring으로 구현 (xml 설정파일과 함께 사용)
```java
public class LogAroundAdvice implements MethodInterceptor {

	@Override
	public Object invoke(MethodInvocation invocation) throws Throwable {

		long start = System.currentTimeMillis();
		
		Object result = invocation.proceed();
		
		long end = System.currentTimeMillis();
		String message = (end - start) + "ms 시간이 걸렸습니다.";
		System.out.println(message);
		
		return result;
	}
	
}
```
- Annotation만을 이용한 구현
```java
// @LogExecutionTime이라는 annotation이 있는 method를 joinPoint로 받음
// 해당 메서드의 앞뒤로 시간을 측정하고 log로 남기는 코드를 삽입

public class LogAroundAdvice implements MethodInterceptor {

	@Override
	public Object invoke(MethodInvocation invocation) throws Throwable {

		long start = System.currentTimeMillis();
		
		Object result = invocation.proceed();
		
		long end = System.currentTimeMillis();
		String message = (end - start) + "ms 시간이 걸렸습니다.";
		System.out.println(message);
		
		return result;
	}
	
}
```

- execution Pointcut 사용 예시
```java
@Component
@Aspect
public class LoggerAspect {
	private Logger log = LoggerFactory.getLogger(this.getClass());
	
	@Around("execution(* board..controller.*Controller.*(..)) or "
			+ "execution(* board..service.*Impl.*(..)) or "
			+ "execution(* board..mapper.*Mapper.*(..))")
	public Object logPrint(ProceedingJoinPoint joinPoint) throws Throwable {
		String type = "";
		String name = joinPoint.getSignature().getDeclaringTypeName();
		if(name.indexOf("Controller") > -1) {
			type = "Controller : ";
		}
		else if(name.indexOf("Service") > -1) {
			type = "Service \t: ";
		}
		else if(name.indexOf("Mapper") > -1) {
			type = "Mapper \t: ";
		}
		log.debug(type + name + "." + joinPoint.getSignature().getName() + "()");
		return joinPoint.proceed();
	}
}
```
