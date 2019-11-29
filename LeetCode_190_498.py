class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans, MASK = 0, 1
        for i in range(32):
            # 从最低位到最高位逐位检查n的第i位是不是为1
            if n & MASK:
                # 把 00000 标记 1
                ans |= 1 << (31 - i)
            # 获取下一位
            MASK <<= 1
        return ans


s = Solution()
print(bin(s.reverseBits(0b0000010100101000001111010011100)))
