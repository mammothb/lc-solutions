from typing import Optional

"""
# Definition for a Node.
"""


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        parent = root
        while parent is not None:
            dummy = Node()
            curr = dummy
            while parent is not None:
                if parent.left is not None:
                    curr.next = parent.left
                    curr = curr.next
                if parent.right is not None:
                    curr.next = parent.right
                    curr = curr.next
                parent = parent.next
            parent = dummy.next
        return root

    def connect_recursive(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return None

        if root.left is not None:
            root.left.next = root.right
            if root.next is not None:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

        return root
