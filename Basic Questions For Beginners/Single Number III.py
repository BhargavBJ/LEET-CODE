class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a = {}
        for n in nums:
            a[n] = a.get(n, 0) + 1
        li =[]
        for num,count in a.items():
            if count == 1:
                li.append(num)
        return li

# Link : https://leetcode.com/problems/single-number-iii/
