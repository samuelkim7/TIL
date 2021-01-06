import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

##########################################################
# DP
# 1904번 - 01타일
# f(n) = f(n-1) + f(n-2)
# num = int(input())
#
# dp = [0] * 1000001
# dp[1] = 1
# dp[2] = 2
#
# for i in range(3, num+1):
#     dp[i] = (dp[i-1] + dp[i-2]) % 15746
#
# print(dp[num])


###########################################################
# DP
# 12865번 - 평범한 배낭
n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        # dp[i][j]: i번째 물건까지 담을 수 있는 경우 j 무게를 담았을 때의 최대 가치
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - w] + v)
print(dp[n][k])