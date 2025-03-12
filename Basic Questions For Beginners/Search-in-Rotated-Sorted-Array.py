from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums :
            return -1
        return nums.index(target)

#Link : https://leetcode.com/problems/search-in-rotated-sorted-array/
