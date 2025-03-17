class Solution:
    def countDigits(self, num: int) -> int:
        org = num
        count = 0
        while org > 0:
            a = org%10
            if num % a == 0:
                count += 1
            org //= 10
        return count