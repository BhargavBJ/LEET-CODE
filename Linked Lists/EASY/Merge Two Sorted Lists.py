# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        li1, li2 = [], []
        while list1:
            li1.append(list1.val)
            list1 = list1.next
        while list2:
            li2.append(list2.val)
            list2 = list2.next
        li1.extend(li2)
        sorted_list = sorted(li1)
        print(sorted_list)
        link = ListNode()
        dummy = link
        for i in sorted_list:
            dummy.next = ListNode(i)
            dummy=dummy.next
        return link.next

# Link: https://leetcode.com/problems/merge-two-sorted-lists/
