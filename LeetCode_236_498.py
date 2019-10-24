# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = None

    def lowestCommonAncestor(self, root, p, q):
        # 如果有根
        def recursion_tree(root):
            # 如果没有根肯定，不是公共祖先
            if root is None:
                return False
            # 调取左右节点的结果
            left_bool = recursion_tree(root.left)
            right_bool = recursion_tree(root.right)
            # 如果当前节点=p,q就标记为True
            # 当前节点有可能是左右
            root_bool = True if root == p or root == q else False
            # 如果有两个是True，就是公共节点
            if root_bool + right_bool + left_bool > 1:
                self.result = root
            # 因为是是递归所以要给其他的递归返回值
            # 如果，当前节点或者左右子节点，有找到了，就返回True
            return root_bool or left_bool or right_bool

        recursion_tree(root)
        return self.result
