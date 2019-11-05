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
        """
        方法？双指针，分为左右，然后不断往里移动压缩，直到相邻，但不能相等。
        移动谁？左右那个高度小就移动谁。
        面积？底 * 高 = 左右两个指针的差 * 当前的最小的高度。
        """
        # 初始化最大盛水量，用于储存
        max_area = 0
        # 双指针
        left_ids = 0
        right_ids = len(height) - 1
        # 当左指针不等于右指针，因为两边都往里走，所以最终肯定会相遇
        while left_ids != right_ids:
            # 左右那边矮，就移动那边指针向里，看看能否遇到大的
            if height[left_ids] < height[right_ids]:
                # 底部等于两个索引的差
                max_area = max(height[left_ids] *
                               (right_ids - left_ids), max_area)
                left_ids += 1
            else:
                max_area = max(height[right_ids] *
                               (right_ids - left_ids), max_area)
                right_ids -= 1
        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([2, 3, 10, 5, 7, 8, 9]))
print(s.maxArea([2, 3, 4, 5, 18, 17, 6]))
