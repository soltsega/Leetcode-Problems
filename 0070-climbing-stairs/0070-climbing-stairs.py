# Type: Recurrence Relations
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<= 2:
            return n
        
        first, second = 1, 2
        for i in range(3, n+1):
            current = first + second
            first = second
            second = current

        return second