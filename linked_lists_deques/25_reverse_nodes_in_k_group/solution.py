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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        dummy.next = head
        left = head
        right = head

        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1

            if count < k:
                return dummy.next

            prev = right
            curr = left
            # Standard reversing
            while count > 0:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count -= 1
            # Move pointers to the next segment
            tail.next = prev
            tail = left
            left = right

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        i = 0
        while curr is not None and i < k:
            curr = curr.next
            i += 1

        if i < k:
            return head

        curr = self.reverseKGroup(curr, k)
        while i > 0:
            next = head.next
            head.next = curr
            curr = head
            head = next
            i -= 1

        return curr
