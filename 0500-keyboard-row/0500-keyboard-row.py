# Technique used:
# Time complexity: O()
# Space complexity: O()

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # Define the three rows of the keyboard
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        
        for word in words:
            # Convert word to lowercase for case-insensitivity
            lower_word = set(word.lower())
            
            # Check if the unique characters of the word form a subset of any single row
            if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
                result.append(word)
                
        return result