from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result

        def dfs(node, result):
            if node.left is not None:
                dfs(node.left, result)
            result.append(node.val)
            if node.right is not None:
                dfs(node.right, result)

        dfs(root, result)
        return result

    def inorder_traversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
