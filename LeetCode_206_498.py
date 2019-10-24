# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        # 创建一個前节点
        new_head = None
        while head:
            # 12345
            # 先把 head 后边的保存下来
            # 2-3-4-5
            head_cp = head.next
            # 1->None，如果不这样就会造成死循环
            head.next = new_head
            # 把 head 接入 new_head 1-None
            new_head = head
            # 再把 head_cp 拉过来
            head = head_cp
        return new_head
