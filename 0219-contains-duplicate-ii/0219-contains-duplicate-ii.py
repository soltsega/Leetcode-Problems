class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, val in enumerate(nums):
            if val in index_map and i-index_map[val]<=k:
                return True
            index_map[val]=i
        return False