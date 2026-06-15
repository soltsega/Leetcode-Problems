# Technique used: DFS
# Time Complexity: O(N*2^N)
# Space Complexity: O(N)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i>= len(nums):
                res.append(subset.copy())
                return

            # to include
            subset.append(nums[i])
            dfs(i+1)

            # To execlude
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
        