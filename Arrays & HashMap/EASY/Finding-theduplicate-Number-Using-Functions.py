from typing import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        duplicates = [num for num, freq in count.items() if freq > 1]
        print("Repeated elements:", duplicates[0])
        return duplicates[0]

#Link : https://leetcode.com/problems/find-the-duplicate-number/description/
