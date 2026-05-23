# Technique used: prime factor reduction or repeated division
# Time complexity: O(log₂ n + log₃ n + log₅ n) -> O(logn)
# Space complexity: O(1)

class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n <= 0:
            return False

        for number in [2,3,5]:
            while n%number == 0:
                n //= number
        return n==1 