class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        index = 0
        if s[index] == "-":
            sign = -1
            index += 1
        elif s[index] == "+":
            index += 1
        res = 0

        while index < len(s) and s[index].isdigit():
            res = res * 10 + int(s[index])
            index += 1
        res *= sign
        if res < -(2**31):
            return -(2**31)
        elif res > 2**31 - 1:
            return 2**31 - 1
        return res
