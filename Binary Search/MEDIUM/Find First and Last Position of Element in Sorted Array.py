class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(nums, target, bias):
            l, r = 0, len(nums)-1
            i = -1
            while l <= r:
                mid = (l+r) // 2

                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    i = mid
                    if bias:
                        r = mid - 1
                    else:
                        l = mid + 1 
            return i
        
        left = search(nums, target, True)
        right = search(nums, target, False)
        return [left, right] 

# Link : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
