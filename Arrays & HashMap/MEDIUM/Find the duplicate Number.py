from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h ={}
        for i,n in enumerate(nums):
            h[n] = h.get(n, 0) + 1
        print(h)
        for i,j in h.items():
            if j>1:
                return i
            

