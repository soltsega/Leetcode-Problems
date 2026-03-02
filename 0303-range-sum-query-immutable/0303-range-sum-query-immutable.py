# Technque Used: Prefix Sum
# Time Complexity: O(N)
# Space Complexity: O(1)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # Declare prefix array
        self.prefix = [0] * (len(nums) + 1)
        # Build prefix array whose length is len(nums) + 1
        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)