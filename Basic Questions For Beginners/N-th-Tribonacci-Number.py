class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        d = 0
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
                #print(a," ",b , "",c,"",d)
        return d