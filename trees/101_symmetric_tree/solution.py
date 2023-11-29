import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None and root1.val == root2.val:
            return self.is_mirror(root1.left, root2.right) and self.is_mirror(
                root1.right, root2.left
            )
        return False

    def is_symmetric_iterative_dfs(self, root: Optional[TreeNode]) -> bool:
        stack = [root.left, root.right]
        while stack:
            node2 = stack.pop()
            node1 = stack.pop()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
        return True

    def is_symmetric_iterative_bfs(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([root.left, root.right])
        while queue:
            node2 = queue.popleft()
            node1 = queue.popleft()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True
