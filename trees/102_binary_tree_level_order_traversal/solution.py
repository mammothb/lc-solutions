import collections
from typing import Deque, List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        result.append([root.val])
        queue = collections.deque()
        queue.append((root.left, 1))
        queue.append((root.right, 1))
        level = []
        last_level = 1
        while queue:
            node, node_level = queue.popleft()
            if node_level > last_level:
                last_level = node_level
                if level:
                    result.append(level)
                level = []
            if node is not None:
                level.append(node.val)
                queue.append((node.left, node_level + 1))
                queue.append((node.right, node_level + 1))
        if level:
            result.append(level)
        return result

    def level_order_optimized(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result: List[List[int]] = []
        level: List[int] = []
        curr_level = 0
        queue: Deque[Tuple[TreeNode, int]] = collections.deque([(root, 0)])
        while queue:
            node, node_level = queue.popleft()
            if node_level > curr_level:
                result.append(level)
                curr_level = node_level
                level = []
            level.append(node.val)
            if node.left is not None:
                queue.append((node.left, node_level + 1))
            if node.right is not None:
                queue.append((node.right, node_level + 1))
        if level:
            result.append(level)
        return result

    def level_order_dfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result: List[List[int]] = []
        stack: List[Tuple[TreeNode, int]] = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if level >= len(result):
                result.append([node.val])
            else:
                result[level].append(node.val)
            if node.right is not None:
                stack.append((node.right, level + 1))
            if node.left is not None:
                stack.append((node.left, level + 1))
        return result
