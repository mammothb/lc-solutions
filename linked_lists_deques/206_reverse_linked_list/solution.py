from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        result = self.reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None
        return result
