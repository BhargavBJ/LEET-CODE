# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        final = li[len(li) // 2 :]
        print(final)
        link = ListNode()
        dummy = link
        for i in final:
            dummy.next = ListNode(i)
            dummy=dummy.next
        return link.next

# Link : https://leetcode.com/problems/middle-of-the-linked-list/description/?env
