# Technique used: Backwards traversal or reverse iteration
# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Start from the last digit and move backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If it's 9, it becomes 0
            digits[i] = 0
            
        # If we reach here, it means we had a carry out of the most significant digit
        # e.g., [9, 9, 9] became [0, 0, 0]. We need to add a 1 at the front.
        return [1] + digits
