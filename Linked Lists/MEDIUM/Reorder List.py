# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        n =[]
        cur =head
        while cur:
            n.append(cur)
            cur = cur.next
        i, j = 0, len(n)-1
        while i<j:
            n[i].next = n[j]
            i+=1
            if i>=j:
                break
            n[j].next=n[i]
            j-=1
        n[i].next = None

#Link : https://leetcode.com/problems/reorder-list/
