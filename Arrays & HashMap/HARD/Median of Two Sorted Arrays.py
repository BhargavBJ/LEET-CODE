from typing import List
class Solution:
    def median(self,a: List[int]) -> float:
        if len(a) % 2 ==0:
            e1 = len(a)//2
            e2 = e1 -1
            m = (a[e1]+a[e2])/2
        else :
            e = len(a)//2
            m = a[e]
        return m
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c =sorted(nums1+nums2)
        return float(self.median(c))
    
#Link : https://leetcode.com/problems/median-of-two-sorted-arrays/description/
