# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li =[]
        while head:
            li.append(head.val)
            head = head.next
        li = sorted(li)
        link = ListNode()
        dummy = link
        for i in li:
            dummy.next = ListNode(i)
            dummy=dummy.next
        return link.next

# Link : https://leetcode.com/problems/sort-list/description/
