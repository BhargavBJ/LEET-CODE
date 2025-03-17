from typing import List
class Solution:
    def series(self,n : int) ->List[int]:
        li = []
        a = 0
        b = 1
        li.append(a)
        li.append(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            li.append(c)
        return li
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        a = self.series(n)
        l1 = len(a)-1
        l2 = l1-1
        s = a[l1]+a[l2]
        return s

#Link : https://leetcode.com/problems/fibonacci-number/
