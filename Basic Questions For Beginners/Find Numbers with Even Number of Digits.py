class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        final = 0
        for i in nums:
            count = 0
            while i:
                count += 1
                i //= 10
            if count % 2 == 0:
                final += 1
        return final

#Link : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
# Time complexity : O(N)
# Space complexity : O(1)
