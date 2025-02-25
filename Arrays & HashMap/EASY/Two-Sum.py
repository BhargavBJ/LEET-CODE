class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l={}
        for i, n in enumerate(nums):
            d = target - n
            if d in l:
                return [l[d],i]
            l[n]=i

#Link : https://leetcode.com/problems/two-sum/description/
