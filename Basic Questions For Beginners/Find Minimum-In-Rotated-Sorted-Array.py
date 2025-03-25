from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Beginner Approach: 
        return min(nums)
        # OR
        a = sorted(nums)
        return a[0]
        #If You don't think you are a beginner try the binary search approach
        ''' Binary Search Approach
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]'''

#Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
