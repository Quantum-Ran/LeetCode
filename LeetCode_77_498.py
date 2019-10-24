class Solution:
    def combine(self, n, k):
        # 要返回的列表
        # 把非常规项排除
        if k == 0 or k > n or n <= 0:
            return [[]]
        # 返回的列表
        res = []

        # 回溯
        def backtrack(b_start, b_list):
            # 出口
            if len(b_list) == k:
                # 长度为 2 的加入返回列表
                res.append(b_list[:])
                return
            # 逻辑
            # 把1-4造出来
            # k - len(h_list) 空余几个格子
            # k - len(h_list) - 1 剩余的数比可取的数量多1
            # n + 1 - (k - len(h_list) - 1)
            for i in range(b_start, n + 1 - (k - len(b_list) - 1)):
                # 过滤加入list
                b_list.append(i)
                # 下一层
                backtrack(i + 1, b_list)
                # 清除数据
                b_list.pop()

        backtrack(1, [])
        return res


s = Solution()
print(s.combine(4, 2))
# 1: 2,3,4
# 2: 3,4
# 3: 4
