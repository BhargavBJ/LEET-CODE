# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        b = 0
        e = n
        while b<e:
            mid = (b+e)//2
            if isBadVersion(mid):
                e = mid
            else:
                b = mid+1
        return b

  # Link : https://leetcode.com/problems/first-bad-version/
