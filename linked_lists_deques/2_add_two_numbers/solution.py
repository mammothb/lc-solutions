from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        result = ListNode()
        curr = result
        carry = 0
        while l1 is not None and l2 is not None:
            carry += l1.val + l2.val
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            carry += l1.val
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
            l1 = l1.next
        while l2 is not None:
            carry += l2.val
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
            l2 = l2.next
        if carry > 0:
            curr.next = ListNode(1)
        return result.next
