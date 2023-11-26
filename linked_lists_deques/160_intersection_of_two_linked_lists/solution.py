from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_intersection_node(
        self, head_a: ListNode, head_b: ListNode
    ) -> Optional[ListNode]:
        set_a = set()
        while head_a is not None:
            set_a.add(id(head_a))
            head_a = head_a.next
        while head_b is not None:
            if id(head_b) in set_a:
                return head_b
            head_b = head_b.next
        return None

    def get_intersection_node_space_optimize(
        self, head_a: ListNode, head_b: ListNode
    ) -> Optional[ListNode]:
        len_a = 0
        len_b = 0
        ptr_a = head_a
        ptr_b = head_b
        while ptr_a is not None:
            len_a += 1
            ptr_a = ptr_a.next
        while ptr_b is not None:
            len_b += 1
            ptr_b = ptr_b.next
        ptr_a = head_a
        ptr_b = head_b
        # Since the intesected portion has the same length, trim the lists
        # so they start with the same amount of non-intersected lengths
        if len_a < len_b:
            while len_a < len_b:
                ptr_b = ptr_b.next
                len_b -= 1
        elif len_b < len_a:
            while len_b < len_a:
                ptr_a = ptr_a.next
                len_a -= 1
        while ptr_a is not None and ptr_b is not None:
            if ptr_a == ptr_b:
                return ptr_a
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next
        return None

    def get_intersection_node_two_pointer(
        self, head_a: ListNode, head_b: ListNode
    ) -> Optional[ListNode]:
        last = head_a
        while last.next is not None:
            last = last.next
        last.next = head_b
        slow = head_a
        fast = head_a
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head_a
                # Find beginning of loop
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                last.next = None
                return slow
        # Unmodify head_a
        last.next = None
        return None
