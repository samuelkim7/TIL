import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
nums = list(map(int, input().split()))

print(n)
print(nums)