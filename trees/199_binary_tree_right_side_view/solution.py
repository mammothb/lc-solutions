import collections
from typing import Deque, List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def right_side_view(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        last_val = 0
        curr_level = 0
        queue: Deque[Tuple[TreeNode, int]] = collections.deque([(root, 0)])
        while queue:
            node, node_level = queue.popleft()
            if node_level > curr_level:
                result.append(last_val)
                curr_level = node_level
            last_val = node.val
            if node.left is not None:
                queue.append((node.left, curr_level + 1))
            if node.right is not None:
                queue.append((node.right, curr_level + 1))
        result.append(last_val)
        return result

    def right_side_view_compact(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        queue = collections.deque([(root, 0)])
        while queue:
            node, node_level = queue.popleft()
            if node.left is not None:
                queue.append((node.left, node_level + 1))
            if node.right is not None:
                queue.append((node.right, node_level + 1))
            # continue if there is another node on the same level to the right
            if queue and node_level == queue[0][1]:
                continue
            result.append(node.val)
        return result

    def right_side_view_dfs(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [(root, 0)]
        # Modified preorder traversal
        while stack:
            node, node_level = stack.pop()
            # Only need to add value for new level since we're traversing from
            # the right first
            if node_level >= len(result):
                result.append(node.val)
            if node.left is not None:
                stack.append((node.left, node_level + 1))
            # process the right node first
            if node.right is not None:
                stack.append((node.right, node_level + 1))
        return result

    def right_side_view_iterative_bfs(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        level = [root]
        while level:
            result.append(level[-1].val)
            level = [
                child
                for node in level
                for child in (node.left, node.right)
                if child is not None
            ]
        return result
