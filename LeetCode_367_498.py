class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        右中位数
        """
        left, right = 1, num
        while left < right:
            middle = left + (right - left + 1) // 2
            # 使用右指针来逼近
            if middle * middle > num:
                right = middle - 1
            else:
                left = middle
        return right * right == num


s = Solution()
print(s.isPerfectSquare(4))