# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li =[]
        while head:
            li.append(head.val)
            head = head.next
        final = len(li) // 2
        del li[final]
        print(li)
        link = ListNode()
        dummy = link
        for i in li:
            dummy.next = ListNode(i)
            dummy=dummy.next
        return link.next    

# Link : https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
