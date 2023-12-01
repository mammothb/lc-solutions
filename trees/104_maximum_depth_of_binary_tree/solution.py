import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        # naive dfs
        def get_depth(root, depth):
            if root is None:
                return depth
            left = get_depth(root.left, depth)
            right = get_depth(root.right, depth)
            return max(left, right) + 1

        return get_depth(root, 0)

    def max_depth_early_stop(self, root: Optional[TreeNode]) -> int:
        def get_depth(root, depth):
            left = get_depth(root.left, depth) if root.left is not None else 0
            right = get_depth(root.right, depth) if root.right is not None else 0
            return max(left, right) + 1

        if root is None:
            return 0
        return get_depth(root, 0)

    def max_depth_bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        queue = collections.deque([root])
        while queue:
            depth += 1
            # process by level
            n_nodes = len(queue)
            for i in range(n_nodes):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return depth
