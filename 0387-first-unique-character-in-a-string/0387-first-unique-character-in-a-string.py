# Technique used: Hash Based Frequency Map 
# Time complexity: O(N) 
# Space complexity: O(1) 

from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1


        