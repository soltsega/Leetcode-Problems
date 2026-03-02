class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        if n <= 1:
            return nums

        sum_of_nums = [0]*n
        sum_of_nums[0] = nums[0]
        for i in range(n):
                sum_of_nums[i] = sum_of_nums[i-1] + nums[i]
        
        return sum_of_nums
        