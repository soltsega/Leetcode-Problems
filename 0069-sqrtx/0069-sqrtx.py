class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        left, right = 2, x // 2
        ans = 1 # Default for x=1, though handled above
        
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            
            if num == x:
                return mid
            elif num < x:
                ans = mid  # mid is a potential floor, keep searching higher
                left = mid + 1
            else:
                right = mid - 1
                
        return ans