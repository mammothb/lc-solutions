from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev is not None and root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True

    def isValidBST_recursive(self, root: Optional[TreeNode]) -> bool:
        def solve(node, min_val, max_val):
            if node is None:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return solve(
                node.left,
                min_val,
                node.val,
            ) and solve(
                node.right,
                node.val,
                max_val,
            )

        return solve(root, float("-inf"), float("inf"))
