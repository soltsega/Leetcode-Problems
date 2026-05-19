# Technique used: Bidirectional Hach Mapping
# Time complexity: O(N + M) which is linear where N is the length of the pattern and M is the number of words

# Space complexity: O(M)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Splits the words 
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_words = {}
        for char, word in zip(pattern, words):
            if char in char_to_words:
                if char_to_words[char] != word:
                    return False
            else:
                # If it's a new character, its word must not be claimed by another char
                if word in char_to_words.values():
                    return False
                char_to_words[char] = word
        
        return True