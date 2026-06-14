# Technique used: Bitmasking or bit manipulation
# Time complexity: O(logN)
# Space complexity: O(1)

class Solution:
    def findComplement(self, num: int) -> int:

        mask = 1

        while mask<num:
            mask = (mask<<1) | 1

        return mask^num
        