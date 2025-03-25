class Solution:
    def hammingWeight(self, n: int) -> int:
        res = ''
        while n>0:
            res += str(n%2)
            n //=2
        count = 0
        for i in range(len(res)):
            if res[i]=='1':
                count += 1
            else:
                continue
        return count

#Link : https://leetcode.com/problems/number-of-1-bits/
