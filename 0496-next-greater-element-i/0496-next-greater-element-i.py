# Technique used: Monotonic Decreasing stack
# Time complexity: O(M+N) where M = len(nums1) and N = len(nums2)
# Space complexity: O(N) + O(N) where N = len(nums2) one for hash map and one for the stack

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        num_greater = {}

        for num in nums2:
            while stack and num>stack[-1]:
                num_greater[stack.pop()] = num
            stack.append(num)

        while stack:
            num_greater[stack.pop()] = -1
        return [num_greater[num] for num in nums1]
        