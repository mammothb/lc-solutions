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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Get mid point with fast slow pointer
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        right_part = slow.next
        slow.next = None

        # Reverse 2nd half of the list
        prev = None
        while right_part is not None:
            next = right_part.next
            right_part.next = prev
            prev = right_part
            right_part = next

        # Merge lists
        curr = head
        while curr is not None and prev is not None:
            next = curr.next
            curr.next = prev
            prev = prev.next
            curr.next.next = next
            curr = curr.next.next
        return head

    def reorderList_2(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        reverse = slow.next
        slow.next = None

        prev = None
        while reverse is not None:
            next = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = next

        dummy = ListNode()
        curr = dummy
        while head is not None and prev is not None:
            curr.next = head
            head = head.next
            curr = curr.next

            curr.next = prev
            prev = prev.next
            curr = curr.next

        if head is not None:
            curr.next = head
        return dummy.next
