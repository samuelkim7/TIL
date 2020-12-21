from typing import *
# <Remove Duplicates from Sorted Array>
# Given a sorted array nums, remove the duplicates in-place
# such that each element appears only once and returns the new length.
def removeDuplicates(self, nums: List[int]) -> int:
    # loop를 돌면서 새로운 요소가 나올 때만 다음 인덱스에 넣기
    j = 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[j] = nums[i + 1]
            j += 1
    nums = nums[0:j]
    return j

# Best Time to Buy and Sell Stock II
# Say you have an array prices for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit.
def maxProfit(self, prices: List[int]) -> int:
    # 만약 다음날 가격이 오늘 보다 높을 경우 오늘 사고 내일 무조건 팜
    _sum = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            _sum += prices[i + 1] - prices[i]
    return _sum

# Rotate Array
# Given an array, rotate the array to the right by k steps, where k is non-negative.
def reverse(self, nums: List[int], start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n

    self.reverse(nums, 0, n - 1)
    self.reverse(nums, 0, k - 1)
    self.reverse(nums, k, n - 1)


