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
        return result


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None

        dummy_large = ListNode()
        dummy_small = ListNode()
        curr_large = dummy_large
        curr_small = dummy_small
        while head is not None:
            if head.val < x:
                curr_small.next = head
                curr_small = curr_small.next
            else:
                curr_large.next = head
                curr_large = curr_large.next
            head = head.next
        curr_small.next = dummy_large.next
        curr_large.next = None

        return dummy_small.next
