# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        # 如果后序遍历为空，证明就没这个节点
        if not inorder:
            return None
        # 因为前序遍历首个元素为根元素，来建立树
        root = TreeNode(preorder[0])
        # 所以找中序遍历的根元素
        root_index = inorder.index(preorder[0])
        # 前序遍历从下标1开始，一共有 root_index个
        # 左子树
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        # 右子树
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        return root
