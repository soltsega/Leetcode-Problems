# Technique used: Two pointer method
# Time complexity: O(N)
# Space complexity: O(1)

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        insert_pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        for i in range(insert_pos, n):
            nums[i] = 0
        return nums