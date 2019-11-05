class Solution:
    def climbStairs(self, n):
        """
        把上第三层台阶，转化为，他是怎么上来的
        1 从 第一阶台阶上来的
        2 从 第二阶台阶上来的
        那上第二层台阶，转化为，他是怎么上来的
        1 从 第一阶台阶上来的
        2 从 第0阶台阶上来的
        那上第一层台阶，转化为，他是怎么上来的
        从 第0阶台阶上来的
        """
        if n <= 2:
            return n
        # 只要记住最后三项就行
        # 初始化
        f1, f2, f3 = 1, 2, 3
        # 要循环 n + 1 - 3
        for i in range(n - 2):
            # 依次往前递进
            f3 = f2 + f1
            f1 = f2
            f2 = f3
        return f3


s = Solution()
print(s.climbStairs(100))
print(s.climbStairs(3))
