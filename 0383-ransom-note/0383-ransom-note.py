class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
            
        # Initialize a frequency array for 26 letters
        char_counts = [0] * 26
        
        # Count characters in magazine
        for char in magazine:
            char_counts[ord(char) - ord('a')] += 1
            
        # Deduct characters for ransomNote
        for char in ransomNote:
            index = ord(char) - ord('a')
            char_counts[index] -= 1
            if char_counts[index] < 0:
                return False
                
        return True