from typing import Optional

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        dummy = Node()
        curr = dummy
        stack = [head]
        while stack:
            head = stack.pop()
            curr.next = head
            head.prev = curr
            curr = curr.next
            if head.next is not None:
                stack.append(head.next)
                head.next = None
            if head.child is not None:
                stack.append(head.child)
                head.child = None
        dummy.next.prev = None
        return dummy.next
