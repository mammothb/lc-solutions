from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if node is None:
                return 0
            left = solve(node.left)
            right = solve(node.right)

            # Result if we allow other nodes to use either node -> left or
            # node -> right
            max_single = max(max(left, right) + node.val, node.val)
            # Result if we're using left -> node -> right as the path
            max_top = max(left + right + node.val, max_single)
            self.res = max(self.res, max_top)
            return max_single

        solve(root)
        return self.res
