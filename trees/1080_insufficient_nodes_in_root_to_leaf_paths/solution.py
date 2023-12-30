from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        def solve(node, curr, limit):
            if node is None:
                return False

            curr += node.val
            if node.left is None and node.right is None:
                return curr >= limit

            left = solve(node.left, curr, limit)
            right = solve(node.right, curr, limit)

            if not left:
                node.left = None
            if not right:
                node.right = None
            return left or right

        result = solve(root, 0, limit)
        if result:
            return root
        return None
