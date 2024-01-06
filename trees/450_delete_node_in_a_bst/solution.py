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

    def deleteNode2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        prev = None
        while curr is not None and curr.val != key:
            prev = curr
            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right

        if prev is None:
            return self._delete(curr)

        if prev.left == curr:
            prev.left = self._delete(curr)
        else:
            prev.right = self._delete(curr)
        return root

    def _delete(self, root):
        if root is None:
            return None
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        next = root.right
        prev = None
        while next.left is not None:
            prev = next
            next = next.left
        next.left = root.left
        if root.right != next:
            prev.left = next.right
            next.right = root.right
        return next
