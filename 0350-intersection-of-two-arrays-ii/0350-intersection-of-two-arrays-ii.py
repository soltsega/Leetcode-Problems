class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # m, n = len(self.num1), len(self.num2)
        counts = Counter(nums1)


        intersection = []
        for i in nums2:
            if counts[i]>0:
                intersection.append(i)
                counts[i] -= 1

        return intersection