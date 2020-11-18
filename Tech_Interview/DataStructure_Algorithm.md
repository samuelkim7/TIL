
## 자료구조 & 알고리즘
- 배열과 Linked List의 차이
- BST와 최악의 시간 복잡도와 최악의 시간이 걸리는 케이스
- Hash Table
- Fibonacci 공식을 recursive 방식과 DP 방식으로 구현시의 차이점
- DFS와 BFS
- 스택 2개를 큐처럼 구현
- 각 정렬의 시간복잡도 비교
<br><br><br>


### 배열과 Linked List의 차이
#### 배열
- 인덱스로 해당 원소에 접근이 가능. 따라서 인덱스로 접근할 경우 O(1)
- 원소를 중간에 삽입할 경우 나머지 원소들의 인덱스도 바뀌어야 함. 또한 정해진 크기를 갖기 때문에 다 찬 경우 내부적으로는 추가가 안 됨
- 원소를 삭제할 경우 O(n)
- 데이터에 접근하는 것이 더 중요한 경우 배열을 사용하는 것이 더 좋음

#### Linked List
- 원소에 접근하는 경우 O(n)
- 삽입과 삭제의 경우 O(n)이며 배열 보다 대체로 더 빠른 편임. 맨 앞이나 맨 뒤에 삽입 또는 삭제할 경우 O(1)
- 따라서 삽입과 삭제가 빈번한 경우 Linked List를 사용하는 것이 더 좋음

#### Java의 ArrayList
- 내부적으로 배열 형태로 데이터를 관리하며 추가, 삭제시 임시 배열을 생성해 데이터를 복사하는 방법을 사용함
- 인덱스로 접근할 경우 O(1). 배열의 끝에서 삽입과 삭제가 일어날 경우 O(1)

### BST와 최악의 시간 복잡도와 최악의 시간이 걸리는 케이스
- Binary Search Tree는 자식 노드가 최대 2개인 이진트리이면서 아래의 두 조건을 만족하는 경우임
  - 왼쪽 부속트리의 모든 노드의 값 < 루트의 값 < 오른쪽 부속트리의 모든 노드의 값
  - 모든 부속트리들도 위의 조건을 만족시킴
- 탐색, 삽입, 삭제 모두 트리의 높이 만큼 시간이 걸림. 즉 O(h). 따라서 평균적인 시간복잡도는 O(logN)
- 하지만 한쪽으로 치우친 skewed tree 형태일 경우 O(n)의 시간복잡도를 갖는다.
  - 마지막 레벨의 왼쪽에서 오른쪽으로 노드를 채운 뒤 다음 레벨로 넘어가는 완전 이진 트리인 경우 이런 최악의 경우를 방지할 수 있다.

### Hash Table
#### 개념
- 연관배열 구조를 이용하여 key에 value(결과 값)을 저장하는 자료구조
- 연관배열 구조: key 1개와 value 1개가 1:1로 연관되어 있는 자료구조. 아래의 명령을 지원함
  - 키와 값이 주어졌을 때 그 키와 값을 저장하는 명령
  - 키가 주어졌을 때 값을 얻는 명령
  - 키와 새로운 값이 주어졌을 때 해당 키에 연관된 값을 새로운 값으로 교체하는 명령
  - 키가 주어졌을 때 해당 키에 연관된 값을 제거하는 명령
- 해시테이블도 위의 명령들을 동일하게 지원함

#### 구조 및 특징
- 해시테이블은 key, hash function, hash, value, bucket(저장소)로 이루어져 있음
- key: 고유한 값이며 hash function의 input이 된다.
- hash function: key를 hash로 바꿔주는 역할을 한다. 서로 다른 key가 같은 hash가 되는 경우를 hash collision이라고 하는데 이 확률을 최대한 줄이는 함수를 만들어야 한다.
- hash: hash function의 결과물이며 bucket에 value와 매칭되어 저장된다.
- value: bucket에 최종적으로 저장되는 값으로 키와 매칭되어 삽입, 삭제, 검색이 가능해야 한다.
- 삽입, 삭제, 검색 모두 O(1)의 시간복잡도를 가짐. 하지만 해시 충돌에 의한 최악의 경우 O(N)이 될 수 있음
- hash collision 해결법1 - Chaining: 저장시 충돌이 발생할 경우 해당 값을 기존 값과 Linked List로 연결하여 저장함
  - 이 경우 삽입은 O(1), 삭제 및 검색 시 O(m/n)의 시간복잡도를 가짐 (m: 키의 수, n: bucket의 길이)
- hash collision 해결법1 - Open Addressing: 저장시 비어있는 hash를 찾아서 데이터를 저장하는 기법. bucket에 비어있는 공간이 부족해질 경우 계속해서 늘려주어야 한다.
  - 이 경우에도 삽입, 삭제, 검색 시 O(m/n)의 시간복잡도를 가짐 (m: 키의 수, n: bucket의 길이)

#### 단점
- 순서를 갖지 않는다.
- 공간 효율성이 떨어진다.
- hash function에 대한 의존도가 높다. 시간복잡도 O(1)은 hash function을 고려하지 않은 것으로서 함수의 복잡도가 높다면 연산의 효율성은 떨어진다.
- [참조 링크](https://velog.io/@cyranocoding)

### Fibonacci 공식을 recursive 방식과 DP 방식으로 구현시의 차이점
### DFS와 BFS

#### 트리에서의 DFS
트리에서 DFS를 사용할 경우 탐색 순서에 따라 3가지 방법으로 나뉜다.
- 전위 순회(Preorder Traversal) : 루트 -> 왼쪽 자식 -> 오른쪽 자식순으로 순회
- 중위 순회(Inorder Traversal): 왼쪽 자식 -> 루트 -> 오른쪽 자식순으로 순화
- 후위 순회(Postorder Traversal): 왼쪽 자식 -> 오른쪽 자식 -> 루트순으로 순회

### 스택 2개를 큐처럼 구현
1. inBox에 데이터를 push한다. - A,B
2. inBox에 있는 데이터를 pop하여 outBox에 push한다. - B,A
3. outBox에 있는 데이터를 pop한다. - A,B 순으로 출력됨

```java
public class Queue {

	private Stack inBox = new Stack();
	private Stack outBox = new Stack();
	
	public void enQueue(Object item) {
		inBox.add(item);
	}
	
	public Object deQueue() {
		
		if (outBox.isEmpty()) {
			while(!inBox.isEmpty()) {
				outBox.push(inBox.pop());
			}
		}
		return outBox.pop();
	}
	
	public static void main(String[] args) {
		Queue queue = new Queue();
		queue.enQueue("A");
		queue.enQueue("B");
		queue.enQueue("C");
		
		System.out.println(queue.deQueue());  // A
		System.out.println(queue.deQueue());  // B
		System.out.println(queue.deQueue());  // C
	}
}
```
- [출처](https://creatordev.tistory.com/83)

### 각 정렬의 시간복잡도 비교


