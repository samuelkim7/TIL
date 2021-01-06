# 정수 삼각형
# 풀이1
def solution(triangle):
    n = len(triangle)
    # dp: 해당 지점까지의 합의 최대값을 배열화한 것
    # 초기화
    dp = [[0] * i for i in range(1, n+1)]
    dp[0][0] = triangle[0][0]

    # 점화식 구현
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][0]
            elif j == i:
                dp[i][j] = dp[i-1][-1] + triangle[i][-1]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return max(dp[n-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))