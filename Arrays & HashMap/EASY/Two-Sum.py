class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
        return l

#Link : https://leetcode.com/problems/two-sum/description/
