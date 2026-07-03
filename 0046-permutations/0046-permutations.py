class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        # Base case: if there's only one element, return it as the only permutation
        if len(nums) == 1:
            return [nums.copy()]
            
        for i in range(len(nums)):
            # Remove the first element to find permutations of the remaining elements
            n = nums.pop(0)
            
            # Recursively find permutations of the sub-array
            perms = self.permute(nums)
            
            # Append the removed element back to all permutations of the sub-array
            for perm in perms:
                perm.append(n)
            
            # Add the generated permutations to our final result
            result.extend(perms)
            
            # Add the element back to the end of nums to restore the state (backtrack)
            nums.append(n)
            
        return result