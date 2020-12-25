import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


# 15969번 - 행복
# n = int(input())
# nums = list(map(int, input().split()))
# print(max(nums) - min(nums))

# 10539번 - 수빈이와 수열
# 해당항까지의 평균값 수열 B가 주어질 때, 이에 따라 수열 A를 구하시오.
# 풀이1
# n = int(input())
# B = list(map(int, input().split()))
#
# A = [B[0]]
# sum_ = A[0]
# for i in range(1, n):
#     a = B[i] * (i+1) - (sum_)
#     A.append(a)
#     sum_ += A[i]
#
# for a in A:
#     print(a, end=' ')

# 풀이2
n = int(input())
B = list(map(int, input().split()))

A = [0 for i in range(n)]
A[0] = B[0]
for i in range(1, n):
    A[i] = B[i] * (i+1) - (sum(A))

for a in A:
    print(a, end=' ')