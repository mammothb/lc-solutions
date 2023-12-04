import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_level_sum(self, root: Optional[TreeNode]) -> int:
        level = 0
        max_sum = float("-inf")
        result = -1
        queue = collections.deque([root])
        while queue:
            n_nodes = len(queue)
            level_sum = 0
            for _ in range(n_nodes):
                node = queue.popleft()
                level_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            level += 1
            if level_sum > max_sum:
                max_sum = level_sum
                result = level
        return result

    def max_level_sum_dfs(self, root: Optional[TreeNode]) -> int:
        sums = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if level >= len(sums):
                sums.append(0)
            sums[level] += node.val
            if node.left is not None:
                stack.append((node.left, level + 1))
            if node.right is not None:
                stack.append((node.right, level + 1))
        max_sum = float("-inf")
        result = -1
        for i, val in enumerate(sums):
            if val > max_sum:
                max_sum = val
                result = i + 1
        return result
