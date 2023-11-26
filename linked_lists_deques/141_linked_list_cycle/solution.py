from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def has_cycle_hash_table(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head is not None:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
