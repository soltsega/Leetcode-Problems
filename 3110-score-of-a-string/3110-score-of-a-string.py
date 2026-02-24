# Technique Used: Iterative accumulation
# Time complexity: O(N)
# Space complexity: O(1)

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[i+1]))
        return res