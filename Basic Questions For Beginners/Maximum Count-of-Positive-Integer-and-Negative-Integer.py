from typing import List 
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p,n=0,0
        for i in nums:
            if i>0:
                p+=1
            if i<0:
                n+=1
            if i==0:
                continue
        if p>n:
            return p
        else:
            return n