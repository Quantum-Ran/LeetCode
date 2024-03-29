# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

# tree_list = [3, 9, 20, None, None, 15, 7]
# for i in tree_list:
#     print(i)
# def create_tree(node):
#
# t = TreeNode()
# t.left = TreeNode()
