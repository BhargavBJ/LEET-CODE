# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from asyncio.windows_events import NULL
from queue import Full
from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr =None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def Traverse(self, head : Optional[ListNode]) ->Optional[ListNode]:
        a = head
        while a:
            print(a.val)
            a = a.next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Create linked list from list
input_list = [1, 2, 3, 4, 5]
linked_list = create_linked_list(input_list)

s = Solution()
s.Traverse(linked_list)
reversed_list = s.reverseList(linked_list)
print("Reversed List:")
s.Traverse(reversed_list)