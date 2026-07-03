class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        minRow = min(op[0] for op in ops)
        minCol = min(op[1] for op in ops)
        return minRow*minCol
