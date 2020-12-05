### Supervised learning
- Supervised learning is where you have input variables (x) and an output variable (Y) and you use an algorithm to learn the mapping function from the input to the output Y = f(X).
- The goal is to approximate the mapping function so well that when you have new input data (x) that you can predict the output variables (Y) for that data.
- Supervised learning requires that the data used to train the algorithm is **already labeled with correct answers**. 
- Supervised learning problems can be further grouped into Regression and Classification problems. The difference between the two tasks is the fact that the dependent attribute is **numerical for regression** and **categorical for classification**.

### Regression and Classification
- A regression problem is when the output variable is a **real or continuous value**, such as “salary” or “weight”.
- A classification problem is when the output variable is **a category**, such as “red” or “blue” or “disease” and “no disease”.
- Classification models include logistic regression, decision tree, random forest, gradient-boosted tree, multilayer perceptron, one-vs-rest, and Naive Bayes.

## TensorFlow
- TensorFlow is an open source software library for numerical computation using data flow graphs.
- Data Flow Graph: Nodes are mathematical operations. Edges represent the multidimensional data arrays (tensors) communicated between them.

- TF basic Mechanics
  - Build graph using TF operations (with placeholder)
  - feed data and run graph
```python
sess.run(op, feed_dict={x: x_data})
```
  - update variables in the graph (and return values)
- placeholder: 값을 지정하지 않고 graph 내에 node만 위치시킴. 그런다음 run 시점에 값을 넘겨주어서 연산을 실행함
- Tensor has Ranks, Shapes, and Types
  - Ranks: Tensor array의 차수
  - Shapes: array 내의 원소 개수와 차수
  - Types: 주로 float32 또는 int32 사용
  
## Linear Regression
- Cost function (Loss fuction): 추정치와 실제 label의 차이를 계산하는 함수
H(x) = Wx + b 일 때,  
cost(W, b) = (H(x) - y)^2의 평균
- 학습의 목표: cost 값을 최소로 만드는 W와 b를 구하는 것

