from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traverse(node, lo, hi):
            if node is None:
                return hi - lo
            left = traverse(node.left, lo, node.val)
            right = traverse(node.right, node.val, hi)
            return min(left, right)

        return traverse(root, float("-inf"), float("inf"))

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        def traverse(node, res):
            if node.left is not None:
                traverse(node.left, res)
            if res[1] is not None:
                res[0] = min(res[0], node.val - res[1])
            res[1] = node.val
            if node.right is not None:
                traverse(node.right, res)

        res = [float("inf"), None]
        traverse(root, res)
        return res[0]

    def getMinimumDifference_iterative(self, root: Optional[TreeNode]) -> int:
        stack = []
        result = float("inf")
        idx = 0
        values = [0, 0]
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            values[idx % 2] = root.val

            root = root.right
            idx += 1
            if idx >= 2:
                result = min(result, abs(values[0] - values[1]))
        return result
