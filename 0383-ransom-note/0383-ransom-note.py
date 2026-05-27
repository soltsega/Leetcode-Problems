class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        char_count = [0]*26

        for char in magazine:
            char_count[ord(char)- ord('a')] += 1
        
        for char in ransomNote:
            index = ord(char)-ord('a')
            char_count[index] -=1

            if char_count[index]<0:
                return False
        return True
