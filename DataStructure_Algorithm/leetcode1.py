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



# Sort List
# Given the head of a linked list, return the list after sorting it in ascending order.
from Cython.Compiler.ExprNodes import ListNode
def sortList(self, head: ListNode) -> ListNode:
    # 연결 리스트 -> 리스트
    p = head
    lst = []
    while p:
        lst.append(p.val)
        p = p.next

    # 정렬
    lst.sort()

    # 리스트 -> 연결 리스트
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next

    return head


# GroupAnagrams
# 풀이1
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # sort each str in the given list
    dic = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        try:
            dic[sorted_s].append(s)
        except KeyError:
            dic[sorted_s] = [s]

    # grouping anagrams
    result = []
    for value in dic.values():
        result.append(value)
    return result

# 풀이2
# When the list class is passed as the default_factory argument,
# then a defaultdict is created with the values that are list.
import collections
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    groups = collections.defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        groups[sorted_word].append(word)
    return groups.values()

groupAnagrams(["eat","tea","tan","ate","nat","bat"])


# Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
def longestPalindrome(self, s: str) -> str:
    if len(s) <= 1:
        return s

    # find palindrome
    i = 0
    while i < len(s):
        for j in range(i + 1):
            temp = s[j:len(s) - i + j]
            if temp == temp[::-1]:
                return temp
        i += 1


# Implement Stack using Queues
from collections import deque
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        temp = deque([x])
        self.q = temp + self.q

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0