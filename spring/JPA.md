### 개념
- Java Persistence API: 자바 객체와 데이터베이스 테이블 간의 매핑을 처리하는 ORM(Object Relational Mapping) 기술의 표준
- JPA Provider: JPA의 표준이 정의한 기능을 구현한 구현체

### 장점
- 편리함 (CRUD 용 SQL을 직접 작성하지 않아도 됨)
- 데이터베이스에 독립적인 개발이 가능함
- 유지보수가 쉬움 (테이블 변경시 JPA 엔티티만 수정하면 됨)

### 단점
- 학습곡선이 크다.
- 특정 데이터베이스의 기능을 사용할 수 없음
- 객체지향 설계가 필요함

### Spring Data JPA
- Repository Interface를 상속하고 정해진 규칙에 맞게 메서드만 작성하면 됨
- 내부적으로 JPA Provider로 Hibernate를 사용함 (이에 따라 적절한 코드가 생성됨)

