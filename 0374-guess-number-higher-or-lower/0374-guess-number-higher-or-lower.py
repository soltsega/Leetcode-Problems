# Technique used: Binary search 
# Time complexity: O(logN) since we have used binary search 
# Space complexity: O(1) since we have used iteration 

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            mid = int(low + (high-low)/2)
            res = guess(mid)

            if res == 0:
                return mid
            elif res == 1:
                low = mid + 1
            else:
                high = mid -1

        return -1
        