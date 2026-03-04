# Technique used: Suffix max
# Time complexity: O(N)
# Space complexity: O(1)

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(arr[i], rightMax)
            arr[i] = rightMax
            rightMax = newMax
        return arr