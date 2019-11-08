# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        node_deque = deque([(1, root)])

        while node_deque:
            depth, node = node_deque.popleft()
            # 都没有
            if not (node.left and node.right):
                return depth
            # 谁有就加入谁继续循环
            if node.left:
                node_deque.append((depth + 1, node.left))
            if node.right:
                node_deque.append((depth + 1, node.right))
        return depth
