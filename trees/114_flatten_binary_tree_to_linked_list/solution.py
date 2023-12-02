from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        tail = None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            if tail is None:
                tail = node
            else:
                tail.right = node
                tail.left = None
                tail = tail.right

    def flatten_recursive(self, root: Optional[TreeNode]) -> None:
        self.prev = None

        def flatten_tree(node):
            # Traverse in reverse preorder
            if node is None:
                return
            if node.right is not None:
                flatten_tree(node.right)
            if node.left is not None:
                flatten_tree(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node

        flatten_tree(root)
