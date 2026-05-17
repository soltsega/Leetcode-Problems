class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer boundaries
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        res = 0
        # We work with the absolute value for easier modulo math, 
        # but track the sign to restore it later.
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10

            if sign == 1:
                if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > 7):
                    return 0
            else:
                if res > abs(INT_MIN) // 10 or (res == abs(INT_MIN) // 10 and pop > 8):
                    return 0
            
            res = (res * 10) + pop
            
        return res * sign