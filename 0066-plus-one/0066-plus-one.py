# Techinque used: Iteration
# Time complexity: O(N)
# Space complexity: O(1) unless all are 9s

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i] += 1
                return digits
            digits[i]=0

        return [1]+ digits
        