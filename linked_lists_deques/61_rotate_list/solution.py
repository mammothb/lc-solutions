from typing import Optional


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
    def rotate_right(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case
        if k == 0 or head is None:
            return head
        tail = None  # Track the last node so we can append the unrotated half to it
        curr = head
        length = 0
        while curr is not None:
            length += 1
            tail = curr
            curr = curr.next
        # when number of rotation = length, the list is unchanged
        k %= length
        if k == 0:
            return head

        i = 0
        curr = head
        while i < length - k - 1:
            curr = curr.next
            i += 1
        # curr is now the end of the unrotated part
        # Store the part to be rotated
        tmp = curr.next
        # Terminate unrotated part
        curr.next = None
        # Append unrotated to rotated
        tail.next = head
        # Head of rotated part is the new head
        head = tmp

        return head

    def rotate_right_optimize(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        # Edge case
        if k == 0 or head is None:
            return head
        tail = None  # Track the last node so we can append the unrotated half to it
        curr = head
        length = 0
        while curr is not None:
            length += 1
            tail = curr
            curr = curr.next
        # when number of rotation = length, the list is unchanged
        k %= length
        if k == 0:
            return head
        # Form a loop
        tail.next = head
        i = 0
        # Iterate 1 more because we're starting at the tail
        while i < length - k:
            tail = tail.next
            i += 1
        head = tail.next
        tail.next = None
        return head

    def rotate_right_optimize_2(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        # Edge case
        if k == 0 or head is None:
            return head

        n = 0
        last = None
        curr = head
        while curr is not None:
            last = curr
            curr = curr.next
            n += 1

        k %= n
        if k == 0:
            return head

        last.next = head
        # Stop at the last node of the rotated node
        while n - k > 0:
            last = last.next
            k += 1

        head = last.next
        last.next = None

        return result

    def rotateRight_3(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        n = 0
        curr = head
        # Tail to append rotated part
        tail = None
        while curr is not None:
            tail = curr
            curr = curr.next
            n += 1

        k %= n
        if k == 0:
            return head

        fast = head
        # Last node of rotated part
        prev = None
        while n - k > 0:
            prev = fast
            fast = fast.next
            k += 1

        prev.next = None
        tail.next = head
        return fast
