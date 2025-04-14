class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = {}
        for n in nums:
            a[n] = a.get(n, 0) + 1
        for num,count in a.items():
            if count == 1:
                return num
