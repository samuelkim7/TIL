
## Java
- [Java의 특징](#Java의-특징)
- 객체 지향 프로그래밍
- Overloading과 Overriding
- Java가 지닌 변수 종류
- Interface와 Abstract Class
- 접근제한자
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

### 객체 지향 프로그래밍 (OOP)
1) 정의: 데이터를 객체로 취급하여 프로그램에 반영한 것이며, 순차적으로 프로그램이 동작하는 기존의 방식과는 다르게 객체와 객체의 상호작용을 통해 프로그램이 동작하는 것을 말한다.  
2) 특징
- 코드의 재사용성이 높다.
- 코드의 변경이 용이하다.
- 직관적인 코드 분석이 가능하다.
- 개발 속도가 향상된다.
- 상속을 통한 장점이 극대화된다.
3) 객체(Object) : 데이터(변수)와 그 데이터에 관련되는 동작(함수)를 포함. 즉 절차, 방법, 기능 모두를 포함한 개념. 같은 성질, 구조, 형태를 갖는 객체를 class로 정의하고 class에 속하는 객체를 해당 class의 인스턴스라고 한다.

### Java가 지닌 변수 종류
0) 변수(Variable): 값을 저장할 수 있는 메모리 상의 공간
1) Primitive type: 변수에 값 자체를 저장함. 스택에 할당됨
- 정수형(byte, short, int, long) / 실수형(float, double) / 문자형(char) / 논리형(boolean)
- Primitive type은 Wrapper Class를 통해 객체로 변형할 수 있다.  
  ex) int -> Integer / char -> Character / float -> Float
2) Reference type: 변수에 객체의 주소를 저장함. 힙에 할당됨
- array, class, interface, enum  
  cf) Wrapper Class: 특정 primitive type을 나타내는 Class. 기본형 타입의 값을 객체가 필요한 곳에 사용 가능.
- Wrapper Class의 생성자는 저장할 기본형 타입 값을 받는다.  
  ex) Integer num = new Integer(30);
- Wrapper 클래스는 산술연산을 위해 정의된 클래스가 아님. 따라서 인스턴스에 저장된 값은 변경이 불가능함. 값 변경을 위해선 다른 값을 저장하는 새로운 객체를 생성해야만 함.
- Boxing: 기본형 변수를 Wrapper Class의 객체로 변경하는 과정. AutoBoxing 가능 (JDK 1.5 이상)  
  ex) Integer num = new Integer(30);  /  Integer num = 61;
- Unboxing: 각각의 객체를 기본형으로 변경하는 과정. AutoUnBoxing 가능 (JDK 1.5 이상)  
  ex) int n = num.intValue();  /  int n = num;

### Overloading과 Overriding

### Interface와 Abstract Class
### 접근제한자
### final, static의 용도와 사용 이유
### 왜 getter, setter 함수를 써야하는지?
### Collections Framework에서 List, Set, Map 등의 특징
### Exception 발생은 컴파일 과정에서 하는가 실행 과정에서 하는가?
### Generic을 사용하는 이점
### JVM의 5가지 메모리 구조
### Garbage Collection
#### Minor Garbage Collection과 Major Garbage Collection의 동작 방식
#### JVM의 young영역에서 survivor부분이 survivor1과 survivor2로 나뉘어져있는 이유?
