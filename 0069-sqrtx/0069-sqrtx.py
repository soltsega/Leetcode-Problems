class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        sqrt_x = 0

        while low <= high:
            mid = (low +high)//2
            if mid*mid <= x:
                sqrt_x = mid
                low += 1
            else:
                high -= 1
        return sqrt_x
        