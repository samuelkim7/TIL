# 더 맵게
# 풀이1
import heapq as hq

def solution1(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer

# 풀이2
import heapq

def solution2(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    mix_cnt = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt


# 디스크 컨트롤러
import heapq

def solution(jobs):
    answer, now, last = 0, 0, -1
    wait, n, count = [], len(jobs), 0

    while count < n:
        for job in jobs:
            if last < job[0] <= now:
                answer += (now - job[0])
                heapq.heappush(wait, job[1])

        if not wait:
            now += 1
            continue

        t = heapq.heappop(wait)
        answer += len(wait) * t
        last = now
        now += t
        count += 1

    return answer // n