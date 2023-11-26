from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        # track start of even-node list to concat with end of odd-node list
        even_start = even
        # For odd number of elements
        # 1 2 3 4 5
        # Initialize:
        # odd = 1, odd.next = 2
        # even = 2, even.next = 3
        # first iter:
        # 1 3 4 5
        # 2 4 5
        # odd = 3, odd.next = 4
        # even = 4, even.next = 5
        # second iter
        # 1 3 5
        # 2 4
        # odd = 5, odd.next = None
        # even = None, even.next = Error
        #
        # For even number of elements
        # 1 2 3 4
        # Initialize:
        # odd = 1, odd.next = 2
        # even = 2, even.next = 3
        # first iter:
        # 1 3 4
        # 2 4
        # odd = 3, odd.next = 4
        # even = 4, even.next = None
        while odd.next is not None and even.next is not None:
            # Skip 1 element
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_start
        return head
