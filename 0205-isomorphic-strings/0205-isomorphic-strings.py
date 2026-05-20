# Technique used: One-to-One hash mapping(bijection)
# Time complexity: O(N) where N is the sum of the length both strings
# Space complexity: O(N)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_st = {}
        map_ts = {}

        for tItem, sItem in zip(t,s):
            if sItem in map_st:
                if map_st[sItem] != tItem:
                    return False
            else:
                map_st[sItem] = tItem
            if tItem in map_ts:
                if map_ts[tItem] != sItem:
                    return False
            else:
                map_ts[tItem] = sItem
        return True