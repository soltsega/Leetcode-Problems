# TEchnique used: Bit manipulation
# Time complexity: O(logN)^2 since we have used nested while loop
# Space complexity: O(1) since we have used iteration

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # determine sign
        negative = (dividend < 0) != (divisor < 0)

        # work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # keep doubling
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient