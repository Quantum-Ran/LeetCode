class Solution:
    def isValid(self, s: str) -> bool:
        """
        方法：栈储存左括号，碰见右括号与栈顶抵消
        """
        # 只有 ） list1 也是空的
        if len(s) % 2 != 0:
            return False
        list1 = []
        for i in s:
            if i in '([{':
                list1.append(i)
            # 必须保证list1有东西才能执行 ')('
            else:
                if list1:
                    if i == ')' and list1[-1] == '(':
                        list1.pop()
                    elif i == ']' and list1[-1] == '[':
                        list1.pop()
                    elif i == '}' and list1[-1] == '{':
                        list1.pop()

        return list1 == []


s = Solution()
print(s.isValid('([)]'))
print(s.isValid(')('))