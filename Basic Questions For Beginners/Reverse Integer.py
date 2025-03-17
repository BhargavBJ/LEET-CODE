class Solution:
    def reverse(self, x: int) -> int:
        a = str(abs(x))
        b = a[::-1]
        res = int(b) if x > 0 else -int(b)
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

#Link : https://leetcode.com/problems/reverse-integer/description/
