from typing import *
from collections import *
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''num = set(nums)
        lon = 0
        for n in nums:
            if (n-1) not in num:
                l = 0
                while n+l in num:
                    l+=1
                lon = max(l,lon)
        return lon '''
        #This solution works but exceeds the time limit by just a fraction 
        #It may work for you but it did not work for me

        #Here is the code That worked for me in leetcode:
        mp = defaultdict(int)
        res = 0
        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res