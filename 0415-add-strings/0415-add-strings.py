class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            # FIX 1: Subtract ord('0') to convert ASCII value to the actual integer
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            current_sum = digit1 + digit2 + carry

            carry = current_sum // 10
            result.append(str(current_sum % 10))

            i -= 1
            j -= 1

        # FIX 2 & 3: Moved outside the loop, and changed to a single negative sign [[::-1]]
        return "".join(result[::-1])