class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = float('-inf')
        
        for num in nums:
            # Skip duplicates to ensure distinct tracking
            if num in (first, second, third):
                continue
                
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
                
        # If the third maximum wasn't updated, return the absolute maximum
        return third if third != float('-inf') else first