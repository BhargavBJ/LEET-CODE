from typing import *
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0] * len(t)
        stack =[]
        for i,n in enumerate(t):
            while stack and n > stack[-1][0]:
                sTemp, sInd = stack.pop() #sTemp = Stack Temperature; sInd = Stack Index
                res[sInd]=(i-sInd)
            stack.append((n,i))
        return res