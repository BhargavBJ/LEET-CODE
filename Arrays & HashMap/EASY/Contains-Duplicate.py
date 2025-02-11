class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        see = set()
        for i in nums:
            if i in see:
                   return True
            see.add(i)
            
        return False
    
#Link : https://leetcode.com/problems/contains-duplicate/description/
