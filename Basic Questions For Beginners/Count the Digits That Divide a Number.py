''' String Approach
class Solution:
    def countDigits(self, num: int) -> int:
        org = str(num)
        count = 0
        for i in org:
            if num%int(i) == 0:
                count += 1
        return count
'''
# Classic Approach
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

#Link : https://leetcode.com/problems/count-the-digits-that-divide-a-number/
