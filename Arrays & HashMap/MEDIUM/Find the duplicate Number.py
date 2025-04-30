from typing import Counter, List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h ={}
        for i,n in enumerate(nums):
            h[n] = h.get(n, 0) + 1
        print(h)
        for i,j in h.items():
            if j>1:
                return i
            


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        duplicates = [num for num, freq in count.items() if freq > 1]
        print("Repeated elements:", duplicates[0])
        return duplicates[0]