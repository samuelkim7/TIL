from typing import *
from Cython.Compiler.ExprNodes import ListNode

# Sort List
# Given the head of a linked list, return the list after sorting it in ascending order.
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