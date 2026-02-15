# Technique used: The property of xor gate
# Time complexity: O(N)
# Space complexity: O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res                         