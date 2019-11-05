class Solution:
    def threeSum(self, nums):
        """
        方法？多指针。目标指针->和 左右指针分别为两端，往中间走
        因为不能重复所以先排序

        """
        # 如果没有原顺序的需求就排序
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        list1 = []
        length_num = len(nums)

        def steps(ids):
            """
            直到找到不重复项
            """
            while nums[ids] == nums[ids - 1]:
                ids += 1
            return ids

        def theSumOfThreeNumber(a, b, c):
            return a + b + c

        # i 是目标指针，所以要除去左右指针的位置
        for i in range(length_num - 2):
            # 目标跟上一个一样就跳过，因为和是一样的，就重复了
            # 但首个没有上一个，所以不能比
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            # 左索引
            left = i + 1
            # 右索引
            right = length_num - 1
            # 右边的一定要大于左边的
            while left < right:
                # 如果左右指针之和比目标小 左指针向右移变大
                if 0 > theSumOfThreeNumber(nums[left], nums[right], nums[i]):
                    left += 1
                # 如果左右指针之和比目标大 右指针向左移变小
                elif 0 < theSumOfThreeNumber(nums[left], nums[right], nums[i]):
                    right -= 1
                elif 0 == theSumOfThreeNumber(nums[left], nums[right], nums[i]):
                    list1.append([nums[i], nums[left], nums[right]])
                    # 因为找到了，所以寻找下一个就是左右指针相向而动，但要之前过滤掉重复的
                    left = steps(left + 1)
                    right = steps(right - 1)

        return list1


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
