# Technique used: Square root factoring
# Time Complexity: O(sqrt(N))
# Space Complexity: O(1)


class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        width = int(math.sqrt(area))

        while area%width!=0:
            width-=1

        return [area//width, width]
        