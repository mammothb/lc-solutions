from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while head is not None:
            if head.next is None:
                curr.next = head
                curr = curr.next
                head = head.next
            else:
                if head.val != head.next.val:
                    curr.next = head
                    curr = curr.next
                    head = head.next
                else:
                    # Skip all duplicated nodes of current head
                    tmp = head.next
                    while tmp is not None and head.val == tmp.val:
                        tmp = tmp.next
                    head = tmp
        curr.next = None
        return dummy.next
