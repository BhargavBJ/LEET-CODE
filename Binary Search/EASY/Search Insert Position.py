class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        b = 0
        e =len(nums)-1
        mid = 0            
        while b<=e :
            mid = (b+e)//2
            if nums[mid]>target:
                e = mid - 1
            elif nums[mid]<target:
                b = mid + 1
            else:
                return mid
        print(b)
        return b

  # Link : https://leetcode.com/problems/search-insert-position/
