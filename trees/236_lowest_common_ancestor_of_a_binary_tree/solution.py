# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root in (p, q):
            return root

        left = None
        right = None
        # Find either p or q in left subtree
        if root.left is not None:
            left = self.lowest_common_ancestor(root.left, p, q)
        # Find either p or q in right subtree
        if root.right is not None:
            right = self.lowest_common_ancestor(root.right, p, q)
        # p and q are found on either side
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right
        return None

    def lowest_common_ancestor_iterative(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        parent = {root: None}
        stack = [root]
        # DFS until both p and q are found
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left is not None:
                parent[node.left] = node
                stack.append(node.left)
            if node.right is not None:
                parent[node.right] = node
                stack.append(node.right)
        p_parents = set()
        # Add nodes in path to p
        while p is not None:
            p_parents.add(p)
            p = parent[p]
        # if q is the LCA, the while loop will not execute
        while q not in p_parents:
            q = parent[q]
        return q
