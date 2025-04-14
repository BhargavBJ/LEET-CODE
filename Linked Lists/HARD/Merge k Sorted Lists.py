# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self,list1: List,list2: List)-> List:
        for i in list2:
            list1.append(i)
        return sorted(list1)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> List:
        final_sorted = []
        for li in lists:
            a=[]
            while li:
                a.append(li.val)
                li = li.next
            final_sorted=self.merge(final_sorted,a)
        print(final_sorted)
        link = ListNode()
        dummy = link
        for i in final_sorted:
            dummy.next = ListNode(i)
            dummy=dummy.next
        return link.next
