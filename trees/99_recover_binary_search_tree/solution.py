from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        node_1 = None
        node_2 = None
        prev = None
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if node_1 is None and (prev is None or prev.val >= root.val):
                node_1 = prev
            if node_1 is not None and prev.val >= root.val:
                node_2 = root
            prev = root
            root = root.right
        node_1.val, node_2.val = node_2.val, node_1.val
