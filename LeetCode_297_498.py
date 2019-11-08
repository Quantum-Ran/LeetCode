# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def rserialize(node, s):
            # 如果是结尾就加 Nones
            if not node:
                s += 'None,'
            else:
                # 如果不是就添加
                s += '{},'.format(node.val)
                # 把左子树放进去
                s = rserialize(node.left, s)
                # 把右子树放进去
                s = rserialize(node.right, s)
            return s

        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(data_list):
            if data_list[0] == "None":
                data_list.popleft()
                return None
            # 先放根
            root = TreeNode(data_list[0])
            # 把根删除
            data_list.popleft()
            # 左子树
            root.left = rdeserialize(data_list)
            # 右子树
            root.right = rdeserialize(data_list)
            return root

        data_deque = deque(data.split(','))
        root = rdeserialize(data_deque)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
