import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def merge_trees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.merge_trees(root1.left, root2.left)
        root1.right = self.merge_trees(root1.right, root2.right)

        return root1

    def merge_trees_stack(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        stack1 = [root1]
        stack2 = [root2]

        while stack1:
            node1 = stack1.pop()
            node2 = stack2.pop()
            node1.val += node2.val

            if node1.left is not None and node2.left is not None:
                stack1.append(node1.left)
                stack2.append(node2.left)
            elif node1.left is None and node2.left is not None:
                node1.left = node2.left
            if node1.right is not None and node2.right is not None:
                stack1.append(node1.right)
                stack2.append(node2.right)
            elif node1.right is None and node2.right is not None:
                node1.right = node2.right
        return root1

    def merge_trees_bfs(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        stack1 = collections.deque([root1])
        stack2 = collections.deque([root2])

        while stack1:
            node1 = stack1.popleft()
            node2 = stack2.popleft()
            node1.val += node2.val

            if node1.left is not None and node2.left is not None:
                stack1.append(node1.left)
                stack2.append(node2.left)
            elif node1.left is None and node2.left is not None:
                node1.left = node2.left
            if node1.right is not None and node2.right is not None:
                stack1.append(node1.right)
                stack2.append(node2.right)
            elif node1.right is None and node2.right is not None:
                node1.right = node2.right
        return root1
