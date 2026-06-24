class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        maxarea = 0

        while l<r:
            w = r-l
            h = min(height[l], height[r])
            area = w*h
            maxarea = max(maxarea, area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return maxarea
        