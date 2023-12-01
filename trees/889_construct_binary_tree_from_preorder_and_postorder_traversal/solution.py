from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def construct_from_pre_post(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        self.pre_map = {val: i for i, val in enumerate(preorder)}
        return self.build(
            0,
            len(preorder) - 1,
            postorder,
        )

    def build(
        self,
        pre_start,
        pre_stop,
        postorder,
    ):
        if pre_start > pre_stop:
            return None
        if pre_start == pre_stop:
            return TreeNode(postorder.pop())
        root = TreeNode(postorder.pop())
        pre_subroot = self.pre_map[postorder[-1]]

        root.right = self.build(pre_subroot, pre_stop, postorder)
        # Since we're popping postorder [pre_subroot, pre_stop],
        # the left child is only left with
        # [pre_start + 1, pre_subroot - 1] element to process
        root.left = self.build(pre_start + 1, pre_subroot - 1, postorder)

        return root

    def construct_from_pre_post_dac(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        """For the tree:
            1
          2   3
         4 5 6 7
        8

        Split the pre and post order like so:

                2|4 8|5
        pre:  1|2 4 8 5|3 6 7
        post: 8 4 5 2|6 7 3|1
              8 4|5|2
        """
        self.pre_map = {val: i for i, val in enumerate(preorder)}
        self.post_map = {val: i for i, val in enumerate(postorder)}
        return self.build_dac(
            preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1
        )

    def build_dac(
        self,
        preorder,
        pre_start,
        pre_stop,
        postorder,
        post_start,
        post_stop,
    ):
        """Given:

                2|4 8|5
        pre:  1|2 4 8 5|3 6 7
        post: 8 4 5 2|6 7 3|1
              8 4|5|2

        To construct the left and right subtree arrays:
        left:
            pre:  2 4 8 5, i.e., [pre_start + 1, index(r_subroot) - 1]
            post: 8 4 5 2, i.e., [post_start, index(l_subroot)]
        right:
            pre:  3 6 7,   i.e., [index(r_subroot), pre_stop]
            post: 6 7 3,   i.e., [index(l_subroot) + 1, post_stop - 1]
        """
        if pre_start > pre_stop:
            return None
        if pre_start == pre_stop:
            return TreeNode(preorder[pre_start])
        root = TreeNode(preorder[pre_start])
        l_subroot_pre = pre_start + 1
        l_subroot_post = self.post_map[preorder[l_subroot_pre]]
        r_subroot_post = post_stop - 1
        r_subroot_pre = self.pre_map[postorder[r_subroot_post]]

        root.left = self.build_dac(
            preorder,
            l_subroot_pre,
            r_subroot_pre - 1,
            postorder,
            post_start,
            l_subroot_post,
        )
        root.right = self.build_dac(
            preorder,
            r_subroot_pre,
            pre_stop,
            postorder,
            l_subroot_post + 1,
            r_subroot_post,
        )
        return root
