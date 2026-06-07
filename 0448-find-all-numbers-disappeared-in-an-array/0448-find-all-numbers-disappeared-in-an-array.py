# Technique used: 
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark indices corresponding to seen numbers as negative
        for num in nums:
            # Get the index that this number points to (0-indexed)
            idx = abs(num) - 1
            
            # If the value at this index is positive, make it negative
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
                
        # Step 2: Collect all indices that still have positive values
        missing_numbers = []
        for i in range(len(nums)):
            # A positive value at index 'i' means the number 'i + 1' is missing
            if nums[i] > 0:
                missing_numbers.append(i + 1)
                
        return missing_numbers