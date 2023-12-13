from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return
            # Root is guaranteed to be minimum by definition, trying to find a
            # node that's bigger than root but smaller than everything else
            if root.val < node.val < res[0]:
                res[0] = node.val
            dfs(node.left)
            dfs(node.right)

        res = [float("inf")]
        dfs(root)
        if res[0] == float("inf"):
            return -1
        return res[0]
