from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes_iterative(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [root]
        count = 0
        while stack:
            root = stack.pop()
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
            count += 1
        return count

    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_depth(node):
            if node is None:
                return 0
            return 1 + get_depth(node.left)

        if root is None:
            return 0
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)

        # In a complete tree, only the last layer maybe be partially filled.
        # If left_depth == right_depth, right subtree maybe partially filled,
        # else, left subtree maybe be partially filled
        if left_depth == right_depth:
            return 2**left_depth + self.countNodes(root.right)
        return 2**right_depth + self.countNodes(root.left)
