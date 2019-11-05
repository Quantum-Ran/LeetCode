class Solution:
    def mySqrt(self, x: int) -> int:
        """

        """
        left = 0
        right = x
        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            middle = left + (right - left + 1) // 2
            square = middle * middle
            if square > x:
                right = middle - 1
            else:
                left = middle
        return left


s = Solution()
print(s.mySqrt(5))
