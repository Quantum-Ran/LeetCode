# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        new_head = ListNode(-1)
        new_head.next = head
        while head.next or head.next.next:
            # 头-2
            new_head.next = head.next
            # 2-1
            b = head.next
            # 1-3
            head.next = head.next.next
            # 2-1
            b.next = head
            # 倒两下
            head = head.next.next
        return new_head
