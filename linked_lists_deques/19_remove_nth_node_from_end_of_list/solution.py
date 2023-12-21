from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = ""
        while self is not None:
            result += f"{self.val}->"
            self = self.next
        return result[:-2]


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        i = 0
        while i < n and fast is not None:
            i += 1
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    def removeNthFromEnd_2(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        fast = head
        while fast is not None and n > 0:
            fast = fast.next
            n -= 1
        if fast is None:
            return head.next

        slow = head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        skip = slow.next.next
        slow.next = None
        slow.next = skip
        return head
