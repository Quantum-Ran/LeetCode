from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        方法：维护一个单调递增的栈，但是遇到小就把之前比他大的全删了
        stack 存放的是当前高度比栈顶高度高的下标
        heights = [0] + heights + [0]
              最矮的需要和0比，算面积也可以不用估计前面，直接借一位
        while 循环不断剔除 stack 里比当前高度大的下标，
              因为只有比当前高才能延伸，所以向后不能延伸了。
        stack.append() 结合追加就能把新的“最矮项”放入栈顶
              如果我一直是栈顶我肯定是最矮的，配合 i 遍历到结尾，
              只要你矮，就能向前向后延伸
        """
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            # 我明白了这里的循环是
            # 当前的高度，比栈顶的小，就可以往前推进
            while stack and heights[stack[-1]] > heights[i]:
                # 把高的下标都删除了
                tmp = stack.pop()
                # heights[tmp]——当前最高
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


s = Solution()
print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
