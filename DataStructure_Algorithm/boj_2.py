import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


###############################################
# 1012번 - 유기농 배추
# 풀이1
# import sys
# sys.setrecursionlimit(100000)
#
# case = int(input())
# for _ in range(case):
#     M, N, K = map(int, input().split())
#     graph = [[0] * M for _ in range(N)]
#     for _ in range(K):
#         y, x = map(int, input().split())
#         graph[x][y] = 1
#
#     def dfs(x, y):
#
#         if x<0 or x>=N or y<0 or y>=M:
#             return False
#
#         if graph[x][y] == 1:
#             graph[x][y] = 0
#             dfs(x-1, y)
#             dfs(x+1, y)
#             dfs(x, y-1)
#             dfs(x, y+1)
#             return True
#         return False
#
#     warm = 0
#     for i in range(N):
#         for j in range(M):
#             if dfs(i, j) == True:
#                 warm += 1
#     print(warm)

#풀이2
# import sys
# sys.setrecursionlimit(100000)
#
# case = int(input())
# for _ in range(case):
#     warm = 0
#     m, n, k = map(int, input().split())
#     graph = [[0] * m for _ in range(n)]
#     for _ in range(k):
#         y, x = map(int, input().split())
#         graph[x][y] = 1
#
#     def dfs(x, y):
#         graph[x][y] = 0
#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, -1, 1]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 1:
#                 dfs(nx, ny)
#     warm = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 1:
#                 dfs(i, j)
#                 warm += 1
#     print(warm)


####################################################
# 1543번 - 문서 검색
# 문서 안에 해당 단어가 중복되지 않게 몇 번 등장하는지 출력
# doc = input()
# word = input()
#
# i = 0
# total = 0
# while len(doc) - i >= len(word):
#     if word == doc[i:i+len(word)]:
#         total += 1
#         i += len(word)
#     else:
#         i += 1
# print(total)


#####################################################
# 2747번 - 피보나치 수
# num = int(input())
#
# def Fib(n):
#     lst = [0, 1]
#     if n <= 1:
#         return lst[n]
#     for i in range(2, n):
#         fib_i = lst[i-1] + lst[i-2]
#         lst.append(fib_i)
#     return lst[n-1] + lst[n-2]
#
# print(Fib(num))

# 풀이2
# n = int(input())
#
# a, b = 0, 1
#
# while n > 0:
#     a, b = b, a + b
#     n -= 1
#
# print(a)


#######################################################
# 1074번 - Z
# 방문 횟수를 result로 놓고, 2^2 * 2^2 배열 방문을 구현한 뒤 재귀 호출 시행
# import sys
# sys.setrecursionlimit(100000)
# result = 0
# N, R, C = map(int, input().split())
#
# def visit(N, r, c):
#     global result
#     if N == 2:
#         if r == R and c == C:
#             print(result)
#             return
#         result += 1
#         if r == R and c+1 == C:
#             print(result)
#             return
#         result += 1
#         if r+1 == R and c == C:
#             print(result)
#             return
#         result += 1
#         if r+1 == R and c+1 == C:
#             print(result)
#             return
#         result += 1
#         return
#     visit(N/2, r, c)
#     visit(N/2, r, c + N/2)
#     visit(N/2, r + N/2, c)
#     visit(N/2, r + N/2, c + N/2)
#
# visit(2 ** N, 0, 0)


#############################################################
# 1260번 - DFS와 BFS
# from collections import deque
# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     v1, v2 = map(int, input().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)
#
# for e in graph:
#     e.sort()
#
# def dfs(v):
#     print(v, end=' ')
#     visited[v] = True
#     for e in graph[v]:
#         if not visited[e]:
#             dfs(e)
#
# def bfs(v):
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if not(visited[v]):
#             visited[v] = True
#             print(v, end=' ')
#             for e in graph[v]:
#                 if not visited[e]:
#                     q.append(e)
#
#
# visited = [False] * (n+1)
# dfs(v)
# print()
# visited = [False] * (n+1)
# bfs(v)
# print()


#######################################################
# 1697번 - 숨바꼭질
from collections import deque
n, k = map(int, input().split())
# 시간과 방문 여부 동시 체크
time = [0] * 100001

def bfs(start, target):
    q = deque([start])
    while q:
        curr = q.popleft()
        if curr == target:
            return time[curr]
        for nex in (curr+1, curr-1, curr*2):
            if 0 <= nex < 100001 and time[nex] == 0:
                time[nex] = time[curr] + 1
                q.append(nex)

print(bfs(n, k))
