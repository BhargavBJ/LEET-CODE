class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c,d = 0,1,1,0
        if n ==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        else:
            for i in range(2,n):
                d = a + b + c
                a = b
                b = c
                c = d
                #print(a," ",b , "",c,"",d) For Trouble Shooting
        return d
#Link: https://leetcode.com/problems/n-th-tribonacci-number/
