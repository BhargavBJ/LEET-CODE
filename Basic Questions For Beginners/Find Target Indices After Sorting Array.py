class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        li = []
        nums = sorted(nums)
        for i in range(0,len(nums)):
            if nums[i] == target:
                li.append(i)
        return li

  # Link : https://leetcode.com/problems/find-target-indices-after-sorting-array/
