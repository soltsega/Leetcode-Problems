# Technique used: Direct index mapping
# Time complexity: O(m*n) + O(m*n) = O(m*n)
# Space complexity: O(m*n)

class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        res = [[0] * c for _ in range(r)]

        for i in range(m * n):
            res[i // c][i % c] = mat[i // n][i % n]

        return res