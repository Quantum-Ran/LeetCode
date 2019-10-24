# class Solution:
#     def maxArea(self, height):
#         # 获得列表的长度
#         height_length = len(height)
#         # 容器的底边是 长度-1
#         bottom_margin = height_length - 1
#         max_area = min(height[0], height[-1]) * bottom_margin
#         # 看看有必要移动吗
#         if bottom_margin == 1:
#             return max_area
#         elif bottom_margin > 1:
#             # 双指针
#             left_index = 0
#             right_index = -1
#             while bottom_margin > 0:
#                 if height[left_index] < height[right_index]:
#                     left_index += 1
#                     bottom_margin -= 1
#                 else:
#                     right_index -= 1
#                     bottom_margin -= 1
#                 max_area = max(min(height[left_index], height[right_index]) * bottom_margin, max_area)
#         return max_area


class Solution:
    def maxArea(self, height):
        # 初始化最大盛水量，用于储存
        max_area = 0
        # 双指针
        left_index = 0
        right_index = len(height) - 1
        # 当左指针不等于右指针，因为两边都往里走，所以最终肯定会相遇
        while left_index != right_index:
            # 左右那边矮，就移动那边指针向里，看看能否遇到大的
            if height[left_index] < height[right_index]:
                # 底部等于两个索引的差
                max_area = max(height[left_index] * (right_index - left_index), max_area)
                left_index += 1
            else:
                max_area = max(height[right_index] * (right_index - left_index), max_area)
                right_index -= 1
        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([2, 3, 10, 5, 7, 8, 9]))
print(s.maxArea([2, 3, 4, 5, 18, 17, 6]))
