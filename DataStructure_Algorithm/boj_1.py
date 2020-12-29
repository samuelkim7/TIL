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
# n = int(input())
# B = list(map(int, input().split()))
#
# A = [0 for i in range(n)]
# A[0] = B[0]
# for i in range(1, n):
#     A[i] = B[i] * (i+1) - (sum(A))
#
# for a in A:
#     print(a, end=' ')

# 이름 궁합 테스트
# 이름을 합친 뒤 숫자로 바꾸어서 궁합이 좋을 두자리의 확률 계산
# 풀이1
# n, m = map(int, input().split())
# name1, name2 = input().split()
#
# dict = {
#     'A': 3, 'B': 2, 'C':1, 'D':2, 'E':4, 'F':3, 'G':1, 'H':3,
#     'I':1, 'J':1, 'K':3, 'L':1, 'M':3, 'N':2, 'O':1, 'P':2, 'Q':2,
#     'R':2, 'S':1, 'T':2, 'U':1, 'V':1, 'W':1, 'X':2, 'Y':2, 'Z':1
# }
#
# nums = []
# for i in range(max(n, m)):
#     try:
#         state = 1
#         nums.append(dict[name1[i]])
#         state = 2
#         nums.append(dict[name2[i]])
#     except IndexError:
#         if state == 1:
#             nums.append(dict[name2[i]])
#         else:
#             continue
#
# while len(nums) > 2:
#     for i in range(len(nums) - 1):
#         nums[i] = (nums[i] + nums[i+1]) % 10
#     nums.pop()
#
# answer = str(nums[0] * 10 + nums[1]) + '%'
# print(answer)

#풀이2
# n, m = map(int, input().split())
# A, B = input().split()
#
# alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,
#        1,2,2,2,1,2,1,1,1,2,2,1]
#
# AB = ''
# min_len = min(n ,m)
# for i in range(min_len):
#     AB += A[i] + B[i]
#
# AB += A[min_len:] + B[min_len:]
#
# lst = [alp[ord(i) - ord('A')] for i in AB]
#
# for i in range(n+m-2):
#     for j in range(n+m-1-i):
#         lst[j] += lst[j+1]
#
# print("{}%".format(lst[0] % 10 * 10 + lst[1] % 10))