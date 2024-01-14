from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode()
        prev = dummy
        curr = head
        while curr is not None and curr.next is not None:
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            prev = curr
            curr = curr.next
        return dummy.next

    def swapPairs_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temp = head.next
        head.next = self.swapPairs_recursive(head.next.next)
        temp.next = head
        return temp

    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode()
        curr = dummy
        while head is not None and head.next is not None:
            next = head.next.next
            curr.next = head.next
            # Break cycle
            head.next = None

            curr.next.next = head
            curr = curr.next.next
            head = next

        # Handle odd numbered list
        if head is not None:
            curr.next = head
            curr.next.next = None
        return dummy.next
