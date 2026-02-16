# Technique used: Grid traversal
# Time Complexity: O(M*N)
# Space complexity: (M*N)

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(img)
        cols = len(img[0])
        
        # Create a result matrix of the same dimensions
        # We can't modify img in-place easily without affecting other calculations
        res = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                total_sum = 0
                count = 0
                
                # Check the 3x3 neighborhood
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        # Boundary check
                        if 0 <= i < rows and 0 <= j < cols:
                            total_sum += img[i][j]
                            count += 1
                
                # Apply the floor average
                res[r][c] = total_sum // count
                
        return res