# Technique used: Backward Pointer method
# Time complexity: O(n,m)
# Space complexity: O(1)
# The time and space complexity can't be optimized anymore; this is the worst case scenario

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Start pointers at the end of the actual data
        p1 = m - 1
        p2 = n - 1
        # Start pointer at the end of the physical array
        p = m + n - 1

        # While there are still elements to compare in both
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are any remaining elements in nums2, copy them over.
        # (We don't need to do this for nums1 because they are already there!)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1