class Solution:
    def threeSum(self, nums):
        # 如果没有原顺序的需求就排序
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        list1 = []
        length_num = len(nums)
        # i 是目标指针，所以要除去左右指针的位置
        for i in range(length_num - 2):
            # 目标跟上一个一样就跳过，但首个不能和上个比
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            # 左索引
            left = i + 1
            # 右索引
            right = length_num - 1
            # 右边的一定要大于左边的
            while left < right:
                # 如果左右指针之和比目标小 左指针向右移变大
                if 0 > nums[left] + nums[right] + nums[i]:
                    left += 1
                # 如果左右指针之和比目标大 右指针向左移变小
                elif 0 < nums[left] + nums[right] + nums[i]:
                    right -= 1
                elif 0 == nums[left] + nums[right] + nums[i]:
                    list1.append([nums[i], nums[left], nums[right]])
                    # 因为找到了，所以寻找下一个就是左右指针相向而动，但要之前过滤掉重复的
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return list1


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
