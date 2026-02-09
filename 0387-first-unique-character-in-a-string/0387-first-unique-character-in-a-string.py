from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        # 1. Build the frequency map
        count = Counter(s)
        
        # 2. Iterate through the string by index
        for i in range(len(s)):
            # Check if this specific character appeared only once
            if count[s[i]] == 1:
                return i
        
        # 3. If no unique character is found, return -1
        return -1