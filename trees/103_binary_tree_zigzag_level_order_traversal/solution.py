import collections
from typing import Deque, List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzag_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        level: List[int] = []
        curr_level = 0
        queue: Deque[Tuple[TreeNode, int]] = collections.deque([(root, 0)])
        while queue:
            node, node_level = queue.popleft()
            if node_level > curr_level:
                result.append(reversed(level) if curr_level % 2 == 1 else level)
                curr_level = node_level
                level = []
            level.append(node.val)
            if node.left is not None:
                queue.append((node.left, node_level + 1))
            if node.right is not None:
                queue.append((node.right, node_level + 1))
        if level:
            result.append(reversed(level) if curr_level % 2 == 1 else level)
        return result

    def zigzag_level_order_no_reverse_bfs(
        self, root: Optional[TreeNode]
    ) -> List[List[int]]:
        if root is None:
            return []
        result = []
        level: List[int] = []
        curr_level = 0
        queue: Deque[Tuple[TreeNode, int]] = collections.deque([(root, 0)])
        # L->R for level % 2 == 0, R->L for level % 2 == 1
        while queue:
            # Check if the next node is on the next level and then set the new
            # level
            if curr_level % 2 == 0 and queue[0][1] > curr_level:
                result.append(level)
                curr_level = queue[0][1]
                level = []
            elif curr_level % 2 == 1 and queue[-1][1] > curr_level:
                result.append(level)
                curr_level = queue[-1][1]
                level = []
            if curr_level % 2 == 0:
                node, _ = queue.popleft()
            else:
                node, _ = queue.pop()
            level.append(node.val)
            # For L->R, append L child and then R child
            if curr_level % 2 == 0:
                if node.left is not None:
                    queue.append((node.left, curr_level + 1))
                if node.right is not None:
                    queue.append((node.right, curr_level + 1))
            # For R->L, prepend R child and then L child
            else:
                if node.right is not None:
                    queue.appendleft((node.right, curr_level + 1))
                if node.left is not None:
                    queue.appendleft((node.left, curr_level + 1))

        if level:
            result.append(level)
        return result
