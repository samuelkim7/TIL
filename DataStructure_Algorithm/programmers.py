# 해시
# 완주하지 못한 선수
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
        
    return participant[-1]
  
# 전화번호 목록
def solution(phone_book):
    # make dict
    phone_nums = {}
    for phone_num in phone_book:
        phone_nums[phone_num] = 1
    
    # check if part of phone_num is in another
    for phone_num in phone_book:
        temp = ''
        for num in phone_num:
            temp += num
            if temp in phone_nums and temp != phone_num:
                return False
    return True
 
# 위장
from collections import Counter
def solution(clothes):
    counter = Counter([kind for item, kind in clothes])
    
    answer = 1
    for kind_num in counter.values():
        answer *= kind_num + 1
    return answer - 1
  
# 베스트앨범
from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre_plays = defaultdict(int)
    genre_songs = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_plays[g] += p
        genre_songs[g].append((i, p))
        
    # sorting
    for (g, p) in sorted(genre_plays.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(genre_songs[g], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer

# 스택/큐
# 기능개발
def solution(progresses, speeds):
    answer = []
    
    while progresses:        
        # development for one day
        for i, speed in enumerate(speeds):
            progresses[i] += speed
            
        # deploy
        deploy = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            deploy += 1
        
        if deploy >= 1:
            answer.append(deploy)
            
    return answer
 
# 프린터
from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(p, i) for i, p in enumerate(priorities)])
    
    while q:
        curr = q.popleft()
        
        if any(curr[0] < num[0] for num in q):
            q.append(curr)
        else:
            answer += 1
            if curr[1] == location:
                return answer
  
# 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    bridge_weight = 0
    
    while bridge:
        answer += 1
        removed = bridge.popleft()
        bridge_weight -= removed
        
        if trucks:
            if bridge_weight + trucks[0] <= weight:
                new_truck = trucks.popleft()
                bridge_weight += new_truck
                bridge.append(new_truck)
            else:
                bridge.append(0)
                
    return answer

# 주식가격
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
  
# 힙
# 더맵게
import heapq as hq
def solution(scoville, K):
    hq.heapify(scoville)
    mix_cnt = 0
    while scoville[0] < K:
        try: 
            first, second = hq.heappop(scoville), hq.heappop(scoville)
            hq.heappush(scoville, first + second*2)
        except IndexError:
            return -1
        mix_cnt += 1
    return mix_cnt

# 디스크 컨트롤러
import heapq
def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    # 시작시간 초기화
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                # 작업 소요시간으로 min heap을 만들기 위해 (t, s) 푸시
                heapq.heappush(heap, (t, s))
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            answer += (time - start)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            time += 1
    return answer//len(jobs)

# 이중우선순위큐
import heapq as hq
def solution(operations):
    answer = []
    heap = []
    
    for op in operations:
        if op[0] == 'I':
            hq.heappush(heap, int(op[2:]))
        else:
            if not heap:
                continue
            elif op[2] == '-':
                hq.heappop(heap)
            else:
                heap = hq.nlargest(len(heap), heap)[1:]
                hq.heapify(heap)
                
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    
    return answer

# 완전탐색
# 소수 찾기
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        coms = list(map(''.join, permutations(list(numbers), i)))
        for num in list(set(coms)):
            if is_prime(int(num)):
                answer.append(int(num))
    return len(set(answer))

# 카펫
def solution(brown, yellow):
    area = brown + yellow
    for b in range(1, area+1):
        if area % b == 0:
            a = area // b
            if 2*a + 2*b == brown + 4:
                return sorted([a,b], reverse=True)
  
# 그리디
# 큰 수 만들기
def solution(number, k):
    answer = []
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
    
        # if last number < new number
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k == 0:
                    break
        
        answer.append(num)
    
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

# 구명보트
def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            answer += 1
            i += 1
            j -= 1
        else:
            answer += 1
            j -= 1
    return answer

# 동적계획법
# 정수 삼각형
def solution(triangle):
    # dp: maximum value of the sum until the element
    dp = [[0]*i for i in range(1, len(triangle)+1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return max(dp[len(triangle)-1])

# BFS/DFS
# 타겟 넘버
answer = 0
def dfs(i, numbers, target, value):
    global answer
    if i == len(numbers) and target == value:
        answer += 1
    
    if i == len(numbers):
        return
    
    dfs(i+1, numbers, target, value + numbers[i])
    dfs(i+1, numbers, target, value - numbers[i])

def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer

# 네트워크
from collections import deque
def bfs(start, computers, visited, n):
    q = deque([start])
    visited[start] = True
    while q:
        curr = q.popleft()
        for i in range(n):
            if computers[curr][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited, n)
            answer += 1
    return answer

# 단어 변환
def solution(begin, target, words):
    # target is not in words
    if target not in words:
        return 0
    
    answer = 0
    q = [begin]
    
    while True:
        temp_q = []
        for word_1 in q:
            if word_1 == target:
                return answer
            
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                if close_words(word_1, word_2):
                    temp_q.append(words.pop(i))
                    
        if not temp_q:
            return 0
        q = temp_q
        answer += 1


def close_words(word1, word2):
    num_same = 0
    for ch1, ch2 in zip(word1, word2):
        if ch1 == ch2:
            num_same += 1
    return len(word1) - num_same == 1

# 이분탐색
# 입국심사
def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        total = 0
        
        for t in times:
            total += mid // t
        
        if total >= n:
            right = mid
        else:
            left = mid + 1
    answer = left
    return answer

# 그래프
# 가장 먼 노드
from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    dists = [-1] * (n+1)
    
    # get the graph
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    # q with starting node 1
    q = deque([1])
    dists[1] = 0
    
    # bfs
    while q:
        curr = q.popleft()
        
        # visit all the connected nodes
        for i in graph[curr]:
            if dists[i] == -1:
                q.append(i)
                dists[i] = dists[curr] + 1
    
    # find nodes with farthest distance
    for dist in dists:
        if dist == max(dists):
            answer += 1
            
    return answer
