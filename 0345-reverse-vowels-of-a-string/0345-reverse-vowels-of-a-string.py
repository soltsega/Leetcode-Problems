# Technique used: Two pointer method
# WE use nested while loops but the inner ones don't reset outer one only extends the movements of those two. 
# Time complexity: O(N)
# Space complexity: O(N)


class Solution:
    def reverseVowels(self, s: str) -> str:
        char = list(s)
        set1 = set("aeiouAEIOU")

        left, right = 0, len(s)-1

        while left < right:

            while left < right and char[left] not in set1:
                left +=1

            while left < right and char[right] not in set1:
                right -= 1

            char[left], char[right] = char[right], char[left]
            left +=1
            right -=1

        return "".join(char)


