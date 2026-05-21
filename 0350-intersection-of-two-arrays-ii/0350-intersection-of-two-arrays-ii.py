# Technique used: Hash Map Frequency Counting
# Time complexity: O(N) overall
# Space complexity: O(N) overall

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Linear time and space complexity 
        counts = Counter(nums1)

        # O(N) space
        intersection = []
        # Linear time complexity
        for i in nums2:
            if counts[i]>0:
                intersection.append(i)
                counts[i] -= 1

        return intersection