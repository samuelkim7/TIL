### 기계 번역의 발전 과정
- RNN 기반
  - RNN(1986), LSTM(1997)
  - Seq2Seq(2014): 소스 문장이 input으로 들어온 뒤, context vector에 해당 문장의 정보를 압축하고 번역된 문장을 output으로 출력. 이때 병목 현상이 발생하여 성능 하락의 원인이 됨 -> 해결방안: 매번 소스 문장에서의 출력 전부를 입력으로 받으면 어떨까?
- Attention 기반
  - 입력 시퀀스 전체에서 정보를 추출하는 방향. encoder의 출력 전부(모든 h값들)를 행렬 형태로 decoder에서 입력으로 받도록함
    - Energy eij = a(s(i-1), hj)
    - Weight aij = softmax(eij)
    - decoder에서 현재의 hidden state 값을 만들기 위해, 이전의 hidden state 값 s와 encoder의 hidden state값 h 각각을 고려한 energy 값을 구한다. 여기서 energy 값은 현재의 단어가 소스 문장의 어떤 단어와 가장 연관성이 있는지를 보여준다.
    - 그런 다음 energy 값의 softmax를 취하여 구한 가중치 값을 토대로 (weighted sum) 현재의 hidden state s 값을 구한다.
    - 이 경우 attention 가중치 a를 통해 각 출력이 어떤 입력 정보에 초점을 두었는지 알 수 있음
  - Seq2Seq with Attention(2015)
  - Transformer(2017). having only attention layers. "Attention is All You Need"
  - GPT: Transformer의 decoder 아키텍처 활용
  - BERT: Transformer의 encoder 아케틱처 활용

## Transformer
- RNN이나 CNN을 전혀 사용하지 않음 
- 임베딩 형태의 input과 Positional Encoding을 더하여 multi-head attention에 넣어줌
- 성능 향상을 위해 residual learning도 사용됨
- 하나의 레이어가 attention과 normalization을 과정을 포함하며, 각 레이어들은 서로 다른 parameter들을 가짐
- 입력값과 출력값의 dimension은 동일함
- encoder의 마지막 layer의 출력값을 decoder의 각 layer에 넣어줌. 이를 통해 해당 단어 출력시 어떤 단어에 더 초점을 두어야하는지가 학습됨
- decoder는 하나의 레이어가 두 개의 attention unit을 가짐. 첫번째 것은 self-attention, 두번째 것은 encoder의 출력값을 받는 attention임
- RNN과의 차이점 중 하나는 각 시점 마다 하나의 단어가 입력되는 것이 아니라 모든 단어들이 positional embedding과 함께 한번에 입력된다는 것이다.

#### Multi-head Attention
- 어떤 단어가 다른 단어들과 얼마의 연관성을 가지고 있는가를 구하는 과정
- 입력값과 출력값의 차원은 동일함
- 세 가지 입력 요소
  - query: 물어보는 주체
  - key: 대상이 되는 각각의 객체들
  - value: 
- 기본적으로 쿼리와 key 값을 matrix multiplication한 후 embedding의 차원으로 나누어서 scailing을 수행하고, softmax를 취한 뒤 value값을 곱해주는 구조
- 여러 개의 attention이 h개 존재하며 이들의 출력값이 concat됨
- mask matrix: attention energy 행렬과 동일한 차원의 matrix가 dot product 되어서 특정 단어를 무시할 수 있도록 해줌
- attention의 세가지 종류: encoder self-attention, masked decoder self-attention, encoder-decoder attention
  - encoder-decoder attention: query는 출력 단어이며, key와 value는 encoder의 마지막 layer의 출력값에 있음

#### Positional Encoding
- sin 함수와 같은 주기 함수를 활용한 공식이 쓰임
- 각 단어의 상대적인 위치 정보를 네트워크에게 입력함
