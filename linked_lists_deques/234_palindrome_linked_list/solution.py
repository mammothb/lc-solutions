from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        ptr_head = head
        while ptr_head is not None:
            reverse = ListNode(ptr_head.val, reverse)
            ptr_head = ptr_head.next
        while head is not None and reverse is not None:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next
        return True

    def is_palindrome_fast_slow_pointer(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # Iterate to the middle of the list
        # Odd number:
        # 0|1|2|3|4
        # s| | | |
        # f| | | |
        #  |s| | |
        #  | |f| |
        #  | |s| |
        #  | | | |f
        # Even number:
        # 0|1|2|3|4|5|
        # s| | | | | |
        # f| | | | | |
        #  |s| | | | |
        #  | |f| | | |
        #  | |s| | | |
        #  | | | |f| |
        #  | | |s| | |
        #  | | | | | |f
        # The slow pointer will end up at the spot where we start to
        # reverse the list
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # Reverse the linked list in-place
        # prev will be the head of the reversed portion
        prev = None
        while slow is not None:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        while head is not None and prev is not None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
