# Technique used:Sliding window
# Time complexity: O(N)
# Space complexity: O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Initialize the sum of the first window
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window across the rest of the array
        for i in range(k, len(nums)):
            # Update sum: Add the new element (nums[i]) 
            # and remove the one that just fell out (nums[i - k])
            current_sum += nums[i] - nums[i - k]
            
            # Keep track of the highest sum found so far
            if current_sum > max_sum:
                max_sum = current_sum
        
        # Return the maximum sum divided by k to get the average
        # Using float() ensures precision, though Python 3 handles this naturally
        return float(max_sum) / k