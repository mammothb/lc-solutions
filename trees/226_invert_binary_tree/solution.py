import collections
from typing import Deque, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue: Deque[Optional[TreeNode]] = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node is not None:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

    def invert_tree_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert_dfs(root)

    def invert_dfs(self, root):
        if root is None:
            return None
        self.invert_dfs(root.left)
        self.invert_dfs(root.right)
        root.left, root.right = root.right, root.left

    def invert_tree_dfs_stack(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return root

    def invertTree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return root
