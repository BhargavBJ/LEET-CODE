from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search Approach : 
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

#Link : https://leetcode.com/problems/search-in-rotated-sorted-array/
        ''' Easy Solution
        if target not in nums :
            return -1
        return nums.index(target)'''
