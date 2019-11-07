from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        方法？回溯
        要模拟从[]加到[1,2,3]
        """
        result = []

        def backtrack(i, nums_p):
            result.append(nums_p)
            # 出口
            if nums_p == nums:
                return
            for j in range(i, len(nums)):
                # 累加的过程
                backtrack(j + 1, nums_p + [nums[j]])

        backtrack(0, [])
        return result


s = Solution()
print(s.subsets([1, 2, 3]))
