# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        li =[]
        while head:
            li.append(head.val)
            head = head.next
        a = len(li)
        remove = a - n
        li.pop(remove)
        print(li)
        link = ListNode()
        dummy = link
        for i in li:
            dummy.next = ListNode(i)
            dummy=dummy.next
        return link.next

