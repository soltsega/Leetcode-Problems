class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = int(a, 2)
        y = int(b, 2)
        
        while y != 0:
            carry = x & y
            
            x = x ^ y
            
            y = carry << 1
            
        return bin(x)[2:]