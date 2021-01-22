from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

### Linked List ###
## Delete Node in a Linked List
# Write a function to delete a node in a singly-linked list.
# You will not be given access to the head of the list,
# instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.
def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next


## Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Follow up: Could you do this in one pass?
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


## 234. Palindrome Linked List
# Given a singly linked list, determine if it is a palindrome.

# converting it into a list. Space: O(n)
def isPalindrome(self, head: ListNode) -> bool:
    lst = []
    while head:
        lst.append(head.val)
        head = head.next

    if lst == lst[::-1]:
        return True
    return False

# just using linked-list. Space
def isPalindrome(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow, rev, rev.next = slow.next, slow, rev
    if fast:
        slow = slow.next

    while rev:
        if rev.val != slow.val:
            return False
        rev, slow = rev.next, slow.next
    return True

### Dynamic Programming ###
## Maximum Subarray
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    largest = [0] * len(nums)
    largest[0] = nums[0]

    for i in range(1, len(nums)):
        largest[i] = max(largest[i - 1] + nums[i], nums[i])

    return max(largest)


### Design ###
## Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            self.min.append(min(x, self.min[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


### Sorting and Searching
## Merge Sorted Array
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1[:] = nums1[:m] + nums2
    nums1.sort()

# Second answer
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        i = j = k = 0
        while j < m and k < n:
            if temp[j] < nums2[k]:
                nums1[i] = temp[j]
                j += 1
                i += 1
            else:
                nums1[i] = nums2[k]
                k += 1
                i += 1

        while j < m:
            nums1[i] = temp[j]
            j += 1
            i += 1
        while k < n:
            nums1[i] = nums2[k]
            k += 1
            i += 1

## First Bad Version
# Implement a function to find the first bad version. You should minimize the number of calls to the API.
def isBadVersion(num):
    pass

def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left