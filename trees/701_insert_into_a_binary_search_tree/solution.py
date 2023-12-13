from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if root is None:
            return new_node
        node = root
        while True:
            if node.val < val:
                if node.right is None:
                    node.right = new_node
                    break
                node = node.right
            else:
                if node.left is None:
                    node.left = new_node
                    break
                node = node.left
        return root

    def insertIntoBST_recursive(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
