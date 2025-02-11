class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        see = set()
        for i in nums:
            if i in see:
                   return True
            see.add(i)
            
        return False
    
a = Solution()
print(a.containsDuplicate([1,1,2,3,4,1,2,3,9]))