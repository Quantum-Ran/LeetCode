from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(b_nums, b_list):
            # 截止条件
            if not b_nums:
                res.append(b_list)
                # 递归永远要有个返回值
                return
            # 逻辑
            for i in range(length_num := len(b_nums)):
                # b_nums = b_nums[:i] + b_nums[i + 1:]
                backtrack(b_nums[:i] + b_nums[i + 1:], b_list + [b_nums[i]])

        backtrack(nums, [])
        return res


s = Solution()
print(s.permute([1, 2, 3]))
