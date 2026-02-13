# Technique used: Dynamic programming/Tabulation
# Time complexity: O(N)
# Space complexity: O(N)


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        sequence = [0,1]
        if n == 0:
            return sequence[0]
        if n == 1:
            return sequence[1]

        for i in range(2, n + 1):
            next_val = sequence[i - 1] + sequence[i - 2] 
            sequence.append(next_val)
        return sequence[n]
        