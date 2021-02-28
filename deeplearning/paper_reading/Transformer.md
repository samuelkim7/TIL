### 기계 번역의 발전 과정
- RNN 기반
  - RNN(1986), LSTM(1997)
  - Seq2Seq(2014): 소스 문장이 input으로 들어온 뒤, context vector에 해당 문장의 정보를 압축하고 번역된 문장을 output으로 출력. 이때 병목 현상이 발생하여 성능 하락의 원인이 됨
- Attention 기반
  - 입력 시퀀스 전체에서 정보를 추출하는 방향. encoder의 출력 전부(모든 h값들)를 행렬 형태로 decoder에서 입력으로 받도록함
    - Energy eij = a(s(i-1), hj)
    - Weight aij = softmax(eij)
    - decoder에서 현재의 hidden state 값을 만들기 위해, 이전의 hidden state 값 s와 encoder의 hidden state값 h 각각을 고려한 energy 값을 구한다. 여기서 energy 값은 현재의 단어가 소스 문장의 어떤 단어와 가장 연관성이 있는지를 보여준다.
    - 그런 다음 energy 값의 softmax를 취하여 구한 가중치 값을 토대로 현재의 hidden state s 값을 구한다.
    - 이 경우 attention 가중치 a를 통해 각 출력이 어떤 입력 정보를 참고했는지 알 수 있음
  - Seq2Seq with Attention(2015)
  - Transformer(2017). Attention is All You Need
  - GPT: Transformer의 decoder 아키텍처 활용
  - BERT: Transformer의 encoder 아케틱처 활용

### Transformer
- RNN이나 CNN을 전혀 사용하지 않음. 
- Attention을 여러 layer에서 반복하여 사용함
- 임베딩 형태의 input과 Positional Encoding을 더하여 attention에 input으로 넣어줌
- 
