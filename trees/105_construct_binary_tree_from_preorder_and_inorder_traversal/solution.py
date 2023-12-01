from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_index = {val: i for i, val in enumerate(inorder)}
        self.preorder_index = 0
        root = self.build(preorder, inorder, 0, len(inorder) - 1)
        return root

    def build(self, preorder, inorder, inorder_start, inorder_stop):
        if inorder_start > inorder_stop:
            return None
        root = TreeNode(preorder[self.preorder_index])
        self.preorder_index += 1
        inorder_root_index = self.inorder_index[root.val]
        root.left = self.build(preorder, inorder, inorder_start, inorder_root_index - 1)
        root.right = self.build(preorder, inorder, inorder_root_index + 1, inorder_stop)
        return root
