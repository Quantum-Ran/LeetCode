class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 建立双指针
        j = 0
        for i in range(len(nums)):
            # 找非零项
            if nums[i] != 0:
                if i != j:
                    # 交换位置
                    nums[j] = nums[i]
                    nums[i] = 0
                # 只有没找非零项的时候不用移位
                j += 1
        return nums


s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))
