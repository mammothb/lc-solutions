from typing import Optional

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        new_head = Node(head.val)
        new_curr = new_head
        old_curr = head
        old_to_new = {head: new_head}
        while old_curr is not None:
            if old_curr.next is not None:
                next_node = Node(old_curr.next.val)
                new_curr.next = next_node
            old_curr = old_curr.next
            new_curr = new_curr.next
            old_to_new[old_curr] = new_curr
        new_curr = new_head
        old_curr = head
        while old_curr is not None:
            new_curr.random = old_to_new[old_curr.random]
            new_curr = new_curr.next
            old_curr = old_curr.next
        return new_head

    def copyRandomList_constant_space(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        # Add duplicate node next to every original node
        curr = head
        while curr is not None:
            next = curr.next

            copy = Node(curr.val)
            curr.next = copy
            copy.next = next

            curr = next

        # Link the random nodes
        curr = head
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Extract the duplicated nodes
        dummy = Node(0)
        new_curr = dummy
        curr = head
        while curr is not None:
            new_curr.next = curr.next
            new_curr = new_curr.next
            curr = curr.next.next
        return dummy.next
