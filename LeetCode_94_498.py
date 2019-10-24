class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         list1 = []
#         # 如果有树的话
#         if root is None:
#             return []
#         # 有左
#         list1 += self.inorderTraversal(root.left)
#         # 有就加值
#         list1.append(root.val)
#         # 有右
#         list1 += self.inorderTraversal(root.right)
#         return list1


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
