from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        vol = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)  
            vol = max(area, vol) 
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return vol