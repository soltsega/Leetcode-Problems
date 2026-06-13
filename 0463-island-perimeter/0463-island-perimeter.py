class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        perimeter = 0

        for i in range(height):
            for j in range(width):
                if grid[i][j]:
                    perimeter +=4

                    if i>0 and grid[i-1][j]==1:
                        perimeter-=2
                    if j>0 and grid[i][j-1]==1:
                        perimeter-=2
            
        return perimeter
        