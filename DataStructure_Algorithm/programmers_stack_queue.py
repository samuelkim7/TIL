# 주식가격
# 풀이 1
from collections import deque
def solution(prices):
    answer = []
    q = deque()

    for e in prices:
        q.append(e)

    while q:
        stay_time = 0
        curr = q.popleft()
        for price in q:
            stay_time += 1
            if curr > price:
                break
        answer.append(stay_time)
    return answer

# 풀이 2
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


# 기능개발
# 풀이 1
def solution(progresses, speeds):
    answer = []
    while progresses:
        # 하루 씩 진행시키기
        for i, speed in enumerate(speeds):
            progresses[i] += speed

        # 진도 100%이면 배포하기
        deploy = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            deploy += 1

        if deploy != 0:
            answer.append(deploy)
    return answer