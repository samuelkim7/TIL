
## Java
- Java의 특징
- JVM과 JAVA 프로그램 실행 과정
- 객체 지향 프로그래밍
- Java가 지닌 변수 종류
- Overloading과 Overriding
- Interface와 Abstract Class
- 접근제어자
- final, static의 용도와 사용 이유
- 왜 getter, setter 함수를 써야하는지?
- Collections Framework에서 List, Set, Map 등의 특징
- Exception 발생은 컴파일 과정에서 하는가 실행 과정에서 하는가?
- Generic을 사용하는 이점
- 디자인 패턴과 싱글
- JVM의 5가지 메모리 구조
- Garbage Collection
  - 필요 이유 GC의 기반 가설
  - Heap 영역 내 객체의 이동과 Minor GC / Major GC의 동작 방식
  - JVM의 young영역에서 survivor부분이 survivor1과 survivor2로 나뉘어져있는 이유?
<br><br><br>

### Java의 특징
- 이식성이 높음 (WORA. Write once, run anywhere): 운영체제에 맞는 자바가상머신(JVM)만 설치하면, 하나의 바이트 코드는 수정하지 않아도 운영체제에 상관없이 작동한다. C 프로그램의 경우 OS에 따라 새롭게 컴파일해야 작동함
- 객체 지향 언어: 아무리 작은 프로그램이라도 객체를 만들기 위한 설계도인 클래스를 작성해야 하고, 객체 간의 연결에 의해 프로그램이 만들어진다. 객체 지향 언어의 특징인 캡슐화, 상속, 다형성이 잘 적용되어 있다. 
- 함수적 프로그래밍 지원: JDK 8 부터 람다식을 지원하여 간결한 코드로 함수 지향 스타일의 코딩을 지원함
- 자동적인 메모리 관리: C 언어의 경우 malloc() 함수로 메모리 할당이 가능하고, 사용된 후 free() 함수를 통해 메모리 할당을 해제해야 함. 만약 이 작업을 잘하지 않으면 메모리가 점유되어 프로그램이 다운되기도 함. 자바에서는 개발자가 메모리에 직접 접근할 수 없도록 설계되어 있음. 객체 생성시 자동적으로 메모리의 heap 영역이 할당되며 Garbage Collector가 자동적으로 사용이 완료된 객체를 제거함
- 멀티쓰레드(Multi-thread) 지원: 동시에 여러 작업을 수행하거나 대용량 파일에 대한 병렬 처리를 위해서 멀티 스레드 프로그래밍이 필요함. 자바는 스레드 생성 및 제어와 관련된 API를 제공하기 때문에 쉽게 멀티 스레드를 구현할 수 있음
- 동적 로딩 지원: 애플리케이션 실행시 모든 객체가 생성되지 않고, 필요 시점에 해당 클래스가 동적으로 로딩되면서 객체가 생성됨. 개발 완료 후에도 해당 클래스만 수정하고 컴파일하면 됨   
<a href="#top">TOP</a>

### JVM과 JAVA 프로그램 실행 과정
- 자바 가상 기계 (JVM): 자바 프로그램 (바이트 코드)은 기계어가 아니므로 운영체제가 실행할 수 없고, 이를 해석하고 실행할 수 있는 가상의 운영체제인 JVM이 필요함. JVM은 운영체제에 맞는 JRE나 JDK를 설치하면 자동으로 설치됨
- C 언어의 경우 소스 파일을 C 컴파일러가 기계어로 번역 후 실행파일이 만들어지면 운영체제가 이를 실행함 
- 그러나 자바에서는 컴파일러(javac.exe, JDK에 포함)가 중간코드인 바이트 코드(.class)를 만드는 일까지만 수행함. 그 이후 java.exe 명령어에 의해 JVM이 구동되면 JVM의 class loader가 class 파일을 JVM 내로 로드함. 이것을 인터프리터(JIT Compiler, JRE에 포함)가 기계코드로의 해석함. 해석된 프로그램은 run-time data area(JVM이 하나의 프로세스로 수행되기 위해 OS로 부터 할당 받은 메모리 영역)에 배치되어 실행됨. 이 과정에서 필요에 따라 JVM이 garbage collection을 수행함  
<a href="#top">TOP</a>

### 객체 지향 프로그래밍
1) 정의: 데이터를 객체로 취급하여 프로그램에 반영한 것이며, 순차적으로 프로그램이 동작하는 기존의 방식과는 다르게 객체와 객체의 상호작용을 통해 프로그램이 동작하는 것을 말한다.  
2) 특징
- 코드의 재사용성이 높다.
- 코드의 변경이 용이하다.
- 직관적인 코드 분석이 가능하다.
- 개발 속도가 향상된다.
- 상속을 통한 장점이 극대화된다.
3) 객체(Object) : 데이터(변수)와 그 데이터에 관련되는 동작(함수)를 포함. 즉 절차, 방법, 기능 모두를 포함한 개념. 같은 성질, 구조, 형태를 갖는 객체를 class로 정의하고 class에 속하는 객체를 해당 class의 인스턴스라고 한다.  
<a href="#top">TOP</a>

### Java가 지닌 변수 종류
0) 변수(Variable): 값을 저장할 수 있는 메모리 상의 공간
1) Primitive type: 변수에 값 자체를 저장함. 스택에 할당됨
- 정수형(byte, short, int, long) / 실수형(float, double) / 문자형(char) / 논리형(boolean)
- Primitive type은 Wrapper Class를 통해 객체로 변형할 수 있다.  
  ex) int -> Integer / char -> Character / float -> Float
2) Reference type: 변수에 객체의 주소를 저장함. 힙에 할당됨
- array, class, interface, enum  
3) Wrapper Class: 특정 primitive type을 나타내는 Class. 기본형 타입의 값을 객체가 필요한 곳에 사용 가능.
- Wrapper Class의 생성자는 저장할 기본형 타입 값을 받는다.  
  ex) Integer num = new Integer(30);
- Wrapper 클래스는 산술연산을 위해 정의된 클래스가 아님. 따라서 인스턴스에 저장된 값은 변경이 불가능함. 값 변경을 위해선 다른 값을 저장하는 새로운 객체를 생성해야만 함.
- Boxing: 기본형 변수를 Wrapper Class의 객체로 변경하는 과정. AutoBoxing 가능 (JDK 1.5 이상)  
  ex) Integer num = new Integer(30);  /  Integer num = 61;
- Unboxing: 각각의 객체를 기본형으로 변경하는 과정. AutoUnBoxing 가능 (JDK 1.5 이상)  
  ex) int n = num.intValue();  /  int n = num;  
<a href="#top">TOP</a>

### Overloading과 Overriding
1) Overloading: 같은 이름의 method를 여러 개 정의하는 것. 매개변수의 타입이 다르거나 개수가 달라야 한다. Return type과 접근제어자는 영향을 주지 않는다.
2) Overriding: 상속에서 나온 개념. 상위 클래스의 메소드를 하위 클래스에서 재정의함. Return type과 매개변수의 타입 및 개수가 같아야 한다.  
<a href="#top">TOP</a>

### Interface와 Abstract Class
1) Interface
- 오직 추상메서드와 상수(public static final)만을 멤버로 갖는다.
- 강력한 강제성으로 인터페이스를 구현하는 객체가 같은 동작을 하도록 보장하는 것이 목적 -> 다형성 극대화
- 사용 예시) DAO를 interface로 만든 후 비즈니스 로직을 구현한 클래스에서 구현체가 아닌 interface를 참조하게 하여 유연한 연결을 갖게 함. 사용하던 DAOImpl이 아닌 새로운 방식으로 DB에 접근하는 DAOImpl을 개발하는 경우 기존의 비즈니스 로직은 변경하지 않고 DAOImpl만 개발하고 이전의 DAOImpl을 없애면 개발이 완료됨
- JAVA8부터는 디폴트 메서드(하위 클래스에서 구현은 선택사항), 정적 메서드도 선언 가능 
2) Abstract Class
- 추상메서드를 하나 이상 가진 클래스
- 동일한 부모를 가지는 일반 클래스들을 묶는 개념으로 상속을 받아서 기능을 확장시키는 것이 목적. 계층 구조를 만들기에 최적
- 하위 일반 클래스들(추상 메서드를 무조건 overriding 해야함)의 공통된 필드와 메소드를 통일하여 일반 클래스 작성 시간 절약
3) 공통점 
- new 연산자로 인스턴스 생성 불가능
- 프로토타입만 있는 추상메서드를 갖는다.
- 사용하기 위해서는 하위클래스에서 추상메서드를 overriding 해야 한다.
4) 차이점
- 추상클래스는 일반 메서드(하위클래스들의 공통 기능으로 정의 가능)를 가질 수 있지만, Interface는 추상 메서드만 갖는다.
- 추상클래스는 단일상속만 가능, 인터페이스는 다중상속 가능  
<a href="#top">TOP</a>

### 접근제어자
(public > protected > default > private)
- public : 접근 제한이 없다(같은 프로젝트 내에 어디서든 사용 가능).
- protected: 같은 패키지 내 또는 해당 클래스를 상속받은 외부 패키지의 클래스에서 접근 가능 
- default: 같은 패키지 내에서만 접근 가능
- private: 해당 클래스 내에서만 접근 가능  
<a href="#top">TOP</a>

### final, static
1) final
- final class: 다른 클래스에서 상속하지 못한다.
- final method: 다른 메소드에서 오버라이딩하지 못한다.
- final variable: 상수가 되어 재할당이 불가능하다.
- cf) finally: try-catch 구문에 붙으며 어떤 경우에도 마지막으로 실행 되는 코드 블록
- cf: finalize(): 특정 Object의 메모리 자원을 반납하는 함수. GC가 실제 작동되기까지는 시간이 걸리므로 사용하지 않는 편이 좋음
2) static
- 클래스가 로딩될 때, 메모리 공간을 할당하는데 처음 설정된 메모리 공간이 변하지 않음을 의미
- 객체를 아무리 많이 만들어도 해당 변수는 하나만 존재(객체와 무관한 키워드)  
<a href="#top">TOP</a>

### 왜 getter, setter 함수를 써야하는지?

### Collections Framework에서 List, Set, Map 등의 특징

### Exception 발생은 컴파일 과정에서 하는가 실행 과정에서 하는가?

### Generic을 사용하는 이점
- 컴파일 시에 객체의 타입을 체크하기 때문에 객체의 타입 안전성을 높이고 형변환의 번거로움을 줄여준다. 
- Collection에 특정 타입의 객체만 추가될 수 있도록 제한함. 이로 인해 collection 내부로 들어온 값이 내가 원하는 타입인지 별도로 체크할 필요가 없음

### 디자인 패턴과 싱글톤
- 디자인 패턴: 공통적인 코드 작성 문제를 해결하는데 도움이 될 수 있는 코드 패턴
- 싱글톤: 전체 프로그램에서 단 하나의 객체만을 생성하고 공유하게 하는 코드 패턴

### JVM의 5가지 메모리 구조

### Garbage Collection
#### 필요 이유와 기반 가설
- 필요 이유: java 프로그램은 메모리를 명시적으로 지정해서 해제하지 않기 때문에 사용된 후 접근 불가능한 상태가 된 객체를 지우는 작업인 Garbage Collection이 필요함
- 기반 가설: 1) 대부분의 객체는 금방 unreachable 상태가 된다. 2) 오래된 객체에서 최근에 생긴 객체로의 참조는 거의 없다. 이 두가지 가설을 기반으로 Heap 영역은 Young 영역과 Old 영역으로 설계됨

#### Heap 영역 내 객체의 이동과 Minor GC / Major GC의 동작 방식
- 객체의 이동: 기본적으로 JVM의 Heap 영역 내에서 객체가 이동하면서 GC가 발생함. 새로 생성된 객체는 YOUNG generation의 Eden 영역에 들어감. Eden 영역이 다 차면 Minor GC가 발생하고, 이때 다른 곳에서 참조되지 않는 객체는 삭제됨. 살아남은 객체는 Young generation의 Survivor 영역 (1, 2가 존재)으로 이동함. Eden 영역이 다 차서 Minor GC가 발생할 때마다 객체는 Survivor1과 Survivor2 사이를 이동하게 되며 더이상 참조되지 않는 객체는 삭제됨. Minor GC에서 살아남은 횟수를 기록한 age bit 값이 임계점(tenuring threshold)을 초과한 객체의 경우 OLD generation으로 이동함 (Promotion). 또는 Survivor 영역이 다 차면 미리 OLD로 이동. OLD generation 내에서는 Major GC (full GC)가 발생하여 객체들이 제거됨. Major GC가 실행되면 GC를 실행하는 스레드 외에 나머지 모든 스레드가 멈춤(stop-the-world). 이 시간 동안 어플리케이션을 멈추기 때문에 WAS에서 문제가 될 수 있음. 이러한 Major GC에 의한 Stop-the-world의 시간을 줄이기 위한 작업이 GC 튜닝임
- Minor GC의 동작 방식: Copy & Scavenge 알고리즘. Eden 영역이 다 차면 reachable한 객체를 식별하여 Survivor 영역으로 복제(copy)하고, Eden 영역을 비움(scavenge)
- GC의 5가지 동작 방식
  - Serial GC: mark-sweep-compaction 방식. Old 영역의 객체를 식별하여 참조되는 객체를 표시(mark)하고, 표시되지 않은 객체를 제거(sweep)한 후, Heap의 앞부분부터 채워나가며 정리(compaction)함
  - Parallel GC: Serial GC와 알고르즘은 같지만 Minor GC를 멀티 스레드로 수행함. Server VM의 기본 GC
  - Parallel Old GC: mark-summary-compaction 방식. 이전 방식들은 단일 스레드가 Old 영역 전체를 훑었지만, 여기서는 멀티 스레드가 Old 영역을 논리적으로 균일하게 나눈 Region 단위로 GC를 수행함
  - CMS GC: Concurrent Mark & Sweep. Initial Mark에서는 STW가 발생하지만, 이 때 marking된 객체를 기준으로 살아있는 객체를 추가 확인하는 Concurrent Mark는 STW가 발생하지 않음. 작업이 멀티 스레드 환경에서 동시진행되기 때문에 stop-the-world 시간이 매우 짧은 대신 memory와 CPU 를 많이 사용하고 compaction 단계가 제공되지 않는다.
  - GI GC : CMS를 개선한 GC. Heap 영역에서 young과 old의 구분을 없애고 전체를 Region으로 재편하여 Region의 상태에 따라 Eden, Survivor, Old, Humongous, Available 영역으로 동적으로 역할이 부여됨. 매우 빠르게 객체를 할당하고 GC한다.
- [참조 Link](https://s2choco.tistory.com/14)

#### JVM의 young영역에서 survivor부분이 survivor1과 survivor2로 나뉘어져있는 이유?
  
<a href="#top">TOP</a>

