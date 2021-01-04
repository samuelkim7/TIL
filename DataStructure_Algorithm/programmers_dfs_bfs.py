# 타겟 넘버
# dfs 풀이1
answer = 0
def dfs(i, numbers, target, value):
    global answer
    # 총합이 타겟과 일치하고 마지막 원소일 경우
    if i == len(numbers) and target == value:
        answer += 1
        return
    # 총합이 타겟과 일치하지 않는 경우
    if i == len(numbers):
        return

    # 다음 인덱스로 넘어가면서 총합에 원소를 더하거나 뺌
    dfs(i + 1, numbers, target, value + numbers[i])
    dfs(i + 1, numbers, target, value - numbers[i])


def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer

# dfs 풀이2
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    if not numbers:
        return 0
    return solution(numbers[:-1], target-numbers[-1]) + solution(numbers[:-1], target+numbers[-1])

# bfs 풀이1
from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque([(0, 0)])
    while q:
        current_sum, idx = q.popleft()
        if idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            q.append([current_sum + numbers[idx], idx + 1])
            q.append([current_sum - numbers[idx], idx + 1])
    return answer


#네트워크
# dfs 풀이1
def dfs(idx, computers, visited, n):
    visited[idx] = True
    for i in range(n):
        if computers[idx][i] == 1 and not visited[i]:
            dfs(i, computers, visited, n)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited, n)
            answer += 1
    return answer

# bfs 풀이1
from collections import deque
def bfs(start, computers, visited, n):
    q = deque([start])
    visited[start] = True
    while q:
        c = q.popleft()
        for i in range(n):
            if computers[c][i] == 1 and not visited[i]:
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