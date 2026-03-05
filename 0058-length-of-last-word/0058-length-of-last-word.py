# Technique used: Iteration
# Time complexity: O(N)
# Space complesity: O(1)

class Solution(object):    
    
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = i = 0
        while i < len(s):
            if s[i] == ' ':
                while i < len(s) and s[i] == ' ':
                    i += 1
                if i == len(s):
                    return length
                length = 0
            else:
                length += 1
                i += 1
        return length
    

