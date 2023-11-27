from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l_height = self.find_height(root.left)
        r_height = self.find_height(root.right)

        return (
            abs(l_height - r_height) <= 1
            and self.is_balanced(root.left)
            and self.is_balanced(root.right)
        )

    def find_height(self, root):
        if root is None:
            return 0
        return max(
            self.find_height(root.left) + 1,
            self.find_height(root.right) + 1,
        )

    def is_balanced_dfs(self, root: Optional[TreeNode]) -> bool:
        return self.find_height_dfs(root) != -1

    def find_height_dfs(self, root):
        if root is None:
            return 0
        l_height = self.find_height_dfs(root.left)
        if l_height == -1:
            return -1
        r_height = self.find_height_dfs(root.right)
        if r_height == -1:
            return -1
        if abs(l_height - r_height) > 1:
            return -1
        return max(l_height, r_height) + 1
