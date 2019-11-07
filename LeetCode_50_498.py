class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        # 平方的倒数
        if n < 0:
            return 1 / self.myPow(x, -n)
        # 如果是奇数
        if n % 2:
            return x * self.myPow(x, n - 1)
        # 不要写 x ** 2
        return self.myPow(x * x, n // 2)


s = Solution()
print(s.myPow(2, -16))
