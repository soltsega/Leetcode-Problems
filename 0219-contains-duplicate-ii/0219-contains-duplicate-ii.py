# Technique used: Hash Map
# Time  Complexity: O(N)
# Space complexity: O(N)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """ index_map = {}

        for i, val in enumerate(nums):
            if val in index_map and i-index_map[val]<=k:
                return True
            index_map[val]=i
        return False """

        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window)>k:
                window.remove(nums[i-k])
        return False