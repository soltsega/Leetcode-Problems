class Solution(object):
    def reverseString(self, string):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(string)-1
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
        return string

        