import collections

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
    def connect(self, root: "Node") -> "Node":
        if root is None:
            return None

        queue = collections.deque([root])
        while queue:
            n_queue = len(queue)
            for i in range(n_queue):
                node = queue.popleft()
                if i < n_queue - 1 and queue:
                    node.next = queue[0]
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return root

    def connect_constant_space(self, root: "Node") -> "Node":
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
