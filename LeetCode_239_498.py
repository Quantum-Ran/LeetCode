from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        方法：双端队列
        """
        res = []
        dq = deque()

        def clear_deque(i_p):
            """
            清理队列只留最大的
            """
            # i_p >= k ——在滑动的过程中，马上要过掉最左侧
            # 如果是dp里的就删除
            if i_p >= k and i_p - k == dq[0]:
                dq.popleft()
            # 重复清除小的
            while dq and nums[i_p] >= nums[dq[-1]]:
                dq.pop()

        # 遍历相当于 k 在滑动
        for i in range(len(nums)):
            # 先清理
            clear_deque(i)
            # 再添加新项
            dq.append(i)
            # i 在 k 的尾端，马上要滑动
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
