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