class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        direction = -1  # -1 means moving up, 1 means moving down

        for ch in s:
            rows[curr_row] += ch

            # Change direction when hitting top or bottom
            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1

            curr_row += direction

        return "".join(rows)
