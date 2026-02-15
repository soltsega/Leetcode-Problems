# Technique used: Succesive division 
# Time complexity: O(logN)
# Space complexity: O(logN)

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        while columnNumber > 0:
            columnNumber -= 1 #this is intended to optimize the indexing to zero since excel is 1 based indexing
            remainder = columnNumber % 26
            result.append(chr(65 + remainder))
            columnNumber //= 26        
        return "".join(reversed(result))