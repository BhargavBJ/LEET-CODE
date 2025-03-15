class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = -31
        #-2**31 <= n <= 2**31 - 1
        while -31<= i and i<= 31:
            if 2**i == n:
                return True
            else:
                i+=1
        return False

        #Bit manipulation Technique:
        return n>0 and (n&(n-1))==0
#Link : https://leetcode.com/problems/power-of-two/description/
