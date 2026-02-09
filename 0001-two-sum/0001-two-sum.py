class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevmap = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in prevmap:
                return [prevmap[complement], i]
            
            prevmap[n] = i