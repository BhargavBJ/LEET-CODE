# Definition for singly-linked list.
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        li =[]
        while head:
            if head.val != val:
                li.append(head.val)
            head = head.next
        print(li)
        link = ListNode()
        dummy = link
        for i in li:
            dummy.next = ListNode(i)
            dummy=dummy.next
        return link.next

#Link : https://leetcode.com/problems/remove-linked-list-elements/
