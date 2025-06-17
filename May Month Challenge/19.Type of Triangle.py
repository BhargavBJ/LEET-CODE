class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        elif nums[0] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        else:
            return "scalene"

# Link: https://leetcode.com/problems/type-of-triangle/description/?envType=daily-question&envId=2025-05-19
