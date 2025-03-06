from typing import List
class Solution:
    def search(self, l: List[int], k: int) -> int:
        i = 0
        e = len(l) - 1
        while i <= e:
            mid = (i + e) // 2  
            if l[mid] > k:
                e = mid - 1
            elif l[mid] < k:
                i = mid + 1
            else:
                return mid
        return -1

#Link :- https://leetcode.com/problems/binary-search/
