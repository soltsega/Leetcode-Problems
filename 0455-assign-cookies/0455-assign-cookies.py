# Technique used: Two pointer technique
# Time complexity: O(NlogN+MlogM+M)
# Space complexity: O(1)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  #O(NlogN)
        s.sort()  #O(MlogM)

        child = 0
        cookie = 0

        #O(M) since it is two pointer
        while cookie<len(s) and child<len(g):
            if s[cookie]>=g[child]:
                child+=1
            cookie+=1
        return child