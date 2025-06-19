# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        b = 0
        e = n
        while b<e:
            mid = (b+e)//2
            if guess(mid) == -1:
                e = mid-1
            elif guess(mid) == 1:
                b = mid + 1
            else:
                return mid
        return e

  # Link : https://leetcode.com/problems/guess-number-higher-or-lower/
