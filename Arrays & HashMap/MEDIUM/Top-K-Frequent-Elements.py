class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
    


# nums = [1,1,1,2,2,2,3] k = 2 RESULT: [1,2]
#Link : https://leetcode.com/problems/top-k-frequent-elements/
