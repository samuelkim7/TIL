# 완주하지 못한 선수
# 풀이1
from collections import Counter

def solution(participant, completion):
    # participant를 map으로 만듦 -> completion으로 카운트 감소 -> count 1인 선수 반환
    count = Counter(participant)

    for e in completion:
        count[e] -= 1

    return list(count.elements())[0]

# 풀이2
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

# 풀이3
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


# 전화번호 목록
# 풀이1
def solution(phone_book):
    # sorting
    phone_book.sort()

    # 바로 다음 것만 체크
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            return False

    return True

# 풀이2
def solution(phone_book):
    # sorting
    phone_book.sort()

    # 바로 다음 것만 체크
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True


# 위장
# 풀이1
from collections import defaultdict
def solution(clothes):
    # 종류별 의상 개수 세기
    counter = defaultdict(int)
    for name, kind in clothes:
        counter[kind] += 1

    # 경우의 수 count
    _sum = 1
    for e in counter.values():
        _sum *= e + 1
    return _sum - 1

# 풀이2
from collections import Counter
from functools import reduce
def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer