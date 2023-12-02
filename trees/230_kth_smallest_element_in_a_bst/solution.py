from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        self.index = k
        self.result = -1

        def find_val(node):
            if node.left is not None:
                find_val(node.left)
            self.index -= 1
            if self.index == 0:
                self.result = node.val
                return
            if node.right is not None:
                find_val(node.right)

        find_val(root)
        return self.result

    def kth_smallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
