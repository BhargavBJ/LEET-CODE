# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        s = set(li)
        l = list(s)
        link = ListNode()
        l = sorted(l)
        dummy = link
        for i in l:
            dummy.next = ListNode(i)
            dummy=dummy.next
        return link.next

# Link : https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
