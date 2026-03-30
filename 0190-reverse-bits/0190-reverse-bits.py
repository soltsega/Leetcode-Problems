# Technique used: Fixed width reversal
# Time complexity: O(N)
# Space complexity: O(1)


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result