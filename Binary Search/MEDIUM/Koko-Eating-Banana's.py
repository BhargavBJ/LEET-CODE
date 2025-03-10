from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l<r:
            m = (l+r)//2
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/m)
            if hrs <= h:
                res = min(res,m)
                r = m-1
            else:
                l = m+1
        return res

# Link : https://leetcode.com/problems/koko-eating-bananas/
