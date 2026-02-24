# Technique used: Iteration/array traversal
# Time comeplexity: O(N)
# Space complexity:O(N)


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) 
        for i in range(n):
            nums.append(nums[i])
        return nums