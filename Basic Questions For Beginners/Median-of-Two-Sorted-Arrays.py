from typing import List 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li =[]
        for i in nums1:
            li.append(i)
        for i in nums2:
            li.append(i)
        l = sorted(li)
        if len(l) % 2 == 0:
            a = len(l)//2
            b = a-1
            s = (l[a]+l[b])/2
            return s
        elif len(l) % 2 ==1:
            a = len(l) //2
            return l[a]

#Link : https://leetcode.com/problems/median-of-two-sorted-arrays/description/
