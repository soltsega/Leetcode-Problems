# Technique used: Hash map
# Time complexity: O(N) where N is the length of characters
# Space complexity: O(k) where k is the number of distinct characters

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        has_odd = False

        for count in freq.values():
            if count%2==0:
                length += count
            else:
                length+=count-1
                has_odd = True
            
        return length+has_odd