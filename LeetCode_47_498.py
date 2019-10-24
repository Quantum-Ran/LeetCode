from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 要去重先排序
        nums.sort()

        def backtrack(b_nums, b_list):
            # b_nums
            # 截止条件
            if not b_nums:
                res.append(b_list)
                # 递归永远要有个返回值
                return
            # 逻辑
            for i in range(length_num := len(b_nums)):
                if i > 0 and b_nums[i] == b_nums[i - 1]:
                    continue
                # b_nums = b_nums[:i] + b_nums[i + 1:]
                backtrack(b_nums[:i] + b_nums[i + 1:], b_list + [b_nums[i]])

        backtrack(nums, [])
        return res


s = Solution()
print(s.permuteUnique([1, 2, 1]))
