# Technique used: Backtracking(DFS)
# Time complexity: O(2^T/M) where T is the target and M is the minimum value in the candidates
# Space complexity: O(T/M) where T and M mean as shown above

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] #global variable

        def dfs(i, cur, total):
            # base case I
            if total == target:
                res.append(cur.copy())
                return
            # base case II
            if i>= len(candidates) or total>target:
                return
            
            # append it to the current collection if illegible
            cur.append(candidates[i])
            # and passing the same index back to the function to iterate over
            dfs(i, cur, total+candidates[i])
            
            # Cleaning up the current collection
            cur.pop()
            # walking through the other branch of the tree
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res

        