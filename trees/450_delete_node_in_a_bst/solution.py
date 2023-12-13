from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root

        if root.left is None:
            new_root = root.right
            del root
            return new_root
        if root.right is None:
            new_root = root.left
            del root
            return new_root

        parent = root
        curr = parent.right
        while curr.left is not None:
            parent = curr
            curr = curr.left
        root.val, curr.val = curr.val, root.val

        if parent == root:
            parent.right = curr.right
        else:
            parent.left = curr.right
        del curr
        return root
