from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def solve(node, p, q):
            if node == p or node == q:
                return node
            if node.val < p.val:
                return solve(node.right, p, q)
            if node.val > q.val:
                return solve(node.left, p, q)
            return node

        if p.val > q.val:
            p, q = q, p

        return solve(root, p, q)

    def lowestCommonAncestor_iterative(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if p.val > q.val:
            p, q = q, p
        while root.val < p.val or root.val > q.val:
            if root.val < p.val:
                root = root.right
            else:
                root = root.left
        return root
