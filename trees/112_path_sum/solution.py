from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(node, target):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return target == node.val
            target -= node.val
            return solve(node.left, target) or solve(node.right, target)

        if root is None:
            return False
        return solve(root, targetSum)
