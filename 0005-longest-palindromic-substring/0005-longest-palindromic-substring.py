class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            # Case 1: Odd length (e.g., "aba")
            len1 = self._expand(s, i, i)
            # Case 2: Even length (e.g., "abba")
            len2 = self._expand(s, i, i + 1)
            
            max_len = max(len1, len2)
            
            # Update the boundaries if a longer palindrome is found
            if max_len > (end - start):
                # We calculate the start and end by splitting the max_len
                # around the center point i
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]

    def _expand(self, s, left, right):
        # Expand outwards as long as characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return the length of the palindrome
        # Formula: (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1