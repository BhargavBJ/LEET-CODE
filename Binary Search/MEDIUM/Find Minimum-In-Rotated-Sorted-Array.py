from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #There's a much easier approach listed under Basic Questions for beginners folder
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

#Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
