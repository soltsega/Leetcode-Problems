# Technique used: Bitwise XOR operator
# Time complexity: O(M+N)~O(2N) 
# Space complexity: O(1) since we have used for only result variable

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for char in s:
            result ^= ord(char)
        
        for char in t:
            result ^= ord(char)

        return chr(result)


        