from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None
        self.inorder_index = {val: i for i, val in enumerate(inorder)}
        root = self.build(
            inorder,
            postorder,
            0,
            len(inorder) - 1,
        )
        return root

    def build(
        self,
        inorder,
        postorder,
        inorder_start,
        inorder_stop,
    ):
        if inorder_start > inorder_stop:
            return None
        root = TreeNode(postorder.pop())
        inorder_root_index = self.inorder_index[root.val]
        root.right = self.build(
            inorder,
            postorder,
            inorder_root_index + 1,
            inorder_stop,
        )
        root.left = self.build(
            inorder,
            postorder,
            inorder_start,
            inorder_root_index - 1,
        )
        return root
