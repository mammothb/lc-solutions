import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([(root, 1)])
        result = 0
        while queue:
            n_nodes = len(queue)
            left = float("inf")
            right = float("-inf")
            for _ in range(n_nodes):
                node, index = queue.popleft()
                left = min(left, index)
                right = max(right, index)
                # Use node numbering scheme similar to heap
                if node.left is not None:
                    queue.append((node.left, 2 * index))
                if node.right is not None:
                    queue.append((node.right, 2 * index + 1))
            result = max(result, right - left + 1)
        return result

    def widthOfBinaryTree_dfs(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level, index, lefts):
            if node is None:
                return 0
            if level >= len(lefts):
                lefts.append(index)
            return max(
                index - lefts[level] + 1,
                dfs(node.left, level + 1, 2 * index, lefts),
                dfs(node.right, level + 1, 2 * index + 1, lefts),
            )

        lefts = []
        return dfs(root, 0, 1, lefts)
