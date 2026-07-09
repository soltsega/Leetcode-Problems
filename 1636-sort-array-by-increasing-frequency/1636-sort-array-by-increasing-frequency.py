# Technique used: Hash Map and Sorting
# Time complexity: O(NlogN+N)=O(NlogN)
# Space complexity: O(N)

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        nums.sort(key=lambda n: (count[n],-n))
        return nums

        