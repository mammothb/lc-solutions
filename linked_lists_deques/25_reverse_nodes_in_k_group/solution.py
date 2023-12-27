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
        def reverse(parent, node, k):
            curr = parent
            next_head = head
            i = 0
            while next_head is not None and i < k:
                curr.next = next_head
                curr = curr.next
                next_head = next_head.next
                i += 1

            if i < k:
                return False, None, None

            prev = None
            curr = head
            while k > 0:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                k -= 1
            parent.next = prev
            return True, head, next_head

        dummy = ListNode()
        res, parent, head = reverse(dummy, head, k)
        while res:
            res, parent, head = reverse(parent, head, k)
        return dummy.next

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
