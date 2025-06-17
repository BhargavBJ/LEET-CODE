class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        li1, li2 = [], []
        for i in range(1,n+1,1):
            if i % m == 0:
                li2.append(i)
            else:
                li1.append(i)

        return sum(li1) - sum(li2)

  # Link : https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/?envType=daily-question&envId=2025-05-27
