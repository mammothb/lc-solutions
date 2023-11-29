from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val < low:
            return self.range_sum_bst(root.right, low, high)
        if root.val > high:
            return self.range_sum_bst(root.left, low, high)
        return (
            root.val
            + self.range_sum_bst(root.left, low, high)
            + self.range_sum_bst(root.right, low, high)
        )
