
## Java
- Java의 특징
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
- JVM의 5가지 메모리 구조
- Garbage Collection
  - Minor Garbage Collection과 Major Garbage Collection의 동작 방식
  - JVM의 young영역에서 survivor부분이 survivor1과 survivor2로 나뉘어져있는 이유?
<br><br><br>

### Java의 특징
- (C++ 대비) 간결하고, 컬렉션을 포함하며, 완전한 객체 지향 언어로서 캡슐화, 상속, 다형성이 잘 적용되어 있음
- WORA (Write once, run anywhere) : 자바가상머신(JVM)만 설치하면 컴퓨터의 운영체제에 상관없이 작동한다.
- 원래는 컴파일러가 코드 분석 후 최적화와 기계코드로의 번역까지 모두 커버함. 그러나 자바에서는 컴파일러(JDK에 포함)가 중간코드인 바이트 코드를 만드는 일까지만 수행함. 그 이후 인터프리터(JIT Compiler, JRE에 포함)가 기계코드로의 번역을 담당함
- Garbage Collector를 통한 자동적인 메모리 관리
- 멀티쓰레드(Multi-thread)를 지원함  
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

### JVM의 5가지 메모리 구조

### Garbage Collection

#### Minor Garbage Collection과 Major Garbage Collection의 동작 방식

#### JVM의 young영역에서 survivor부분이 survivor1과 survivor2로 나뉘어져있는 이유?

