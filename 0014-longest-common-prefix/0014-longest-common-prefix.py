class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # We use the first word as our reference point
        first_word = strs[0]
        
        for i in range(len(first_word)):
            char = first_word[i]
            
            # Compare this character with the same index in all other words
            for j in range(1, len(strs)):
                # If the current word is shorter than 'i' or characters don't match
                if i == len(strs[j]) or strs[j][i] != char:
                    # Return everything up to the mismatch
                    return first_word[:i]
        
        # If we finish the loop, the entire first word is the prefix
        return first_word