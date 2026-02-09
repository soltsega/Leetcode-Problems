# Technique used: Early exit
# Time complexity: O(N)
# Space complexity: O(N)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False