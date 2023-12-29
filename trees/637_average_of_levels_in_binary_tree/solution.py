import collections
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []

        queue = collections.deque([root])
        while queue:
            n_queue = len(queue)
            result.append(0)
            for _ in range(n_queue):
                node = queue.popleft()
                result[-1] += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result[-1] /= n_queue
        return result
