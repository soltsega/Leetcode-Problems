class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        res = []

        is_negative = num<0
        num = abs(num)
        while num>0:
            res.append(str(num%7))
            num//=7
        string = "".join(res[::-1])

        return f"-{string}" if is_negative else string