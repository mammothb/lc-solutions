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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        other = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(other)

        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode()
        curr = dummy
        while left is not None and right is not None:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left is not None:
            curr.next = left
        if right is not None:
            curr.next = right
        return dummy.next
