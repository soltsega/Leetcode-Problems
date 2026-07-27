class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)
        return rev==rev[::-1]