from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_between(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(next=head)
        orig_stop = dummy
        i = 0
        while i < left - 1:
            orig_stop = orig_stop.next
            i += 1
        tail = orig_stop.next
        # reverse incrementally
        while i < right - 1:
            # For example, if we have
            # 0->1->2->3->4
            #    ^  ^
            #    |  tail
            #    orig_stop

            # save orig_stop.next since we're going to re assign it
            tmp = orig_stop.next
            # assign orig_stop.next to 3, skipping 2
            orig_stop.next = tail.next
            # link 2 to 4
            tail.next = tail.next.next
            # link 3 to 2
            orig_stop.next.next = tmp
            i += 1
        return dummy.next
