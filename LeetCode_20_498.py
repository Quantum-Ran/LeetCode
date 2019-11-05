class Solution:
    def isValid(self, s: str) -> bool:
        """
        方法：栈储存左括号，碰见右括号与栈顶抵消
        """
        