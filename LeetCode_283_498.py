class Solution:
    def moveZeroes(self, nums):
        """
        方法?双指针，一个找非0项，另一个不动，
        开始 i,j指向同一个位置 0 。如果 nums[i]!= 0 且 i = j，i和j同步。=> 在j和j之前都是非0项
        只要有 0，j就停了，i继续往后找。
        i和j如果相聚差距很大，就证明i到j存在很多0
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
                # 如果都是非0，i和j 就是同步的。如果是异步，证明j就停留在
                j += 1
        return nums


s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))
