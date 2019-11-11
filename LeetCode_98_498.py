# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> Optional[bool]:
        """
        不能只判断树的左右节点，还要有上下界
        """

        def check(node, lower, upper):
            if not node:
                return True
            if lower >= node.val or node.val >= upper:
                return False
            return check(
                node.left,
                lower,
                node.val) and check(
                node.right,
                node.val,
                upper)

        return check(root, float('-inf'), float('inf'))


t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(3)
s = Solution()
print(s.isValidBST(t))
