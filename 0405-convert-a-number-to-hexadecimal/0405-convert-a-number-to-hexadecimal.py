# Technique used: Bit manipulation
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        num &= 0xffffffff

        res = []

        while num:
            res.append(hex_chars[num & 0xf])
            num >>= 4

        return "".join(reversed(res))