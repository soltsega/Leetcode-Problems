# Technique used: Brian Kernighan’s Algorithm
# Time complexity: O(K) where K is the number of set bits or 1's
# Space complexity: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n &= n-1
            count += 1
        return count