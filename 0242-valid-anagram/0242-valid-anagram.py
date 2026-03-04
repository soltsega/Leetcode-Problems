# Technique used: Hash Table(Array)
# Time complesity: O(N+M)
# Space complesity: O(1)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:  #All the elements of count array will be 0 if array t and s are the same as we are decrementing each time we add 1 
                return False
        return True