# Technique used: Two pointer method/ In place manipulation
# Time complexity: O(N)
# Space complexity: O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
