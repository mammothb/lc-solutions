import collections
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order_bottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = collections.deque()
        queue = collections.deque([root])
        while queue:
            level = []
            n_nodes = len(queue)
            for _ in range(n_nodes):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.appendleft(level)
        return list(result)

    def level_order_bottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, level, result):
            if level + 1 > len(result):
                result.appendleft([])
            result[-(level + 1)].append(node.val)
            if node.left is not None:
                dfs(node.left, level + 1, result)
            if node.right is not None:
                dfs(node.right, level + 1, result)

        if root is None:
            return []
        result = collections.deque()
        dfs(root, 0, result)
        return list(result)
