from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_to_bst(self, nums: List[int]) -> Optional[TreeNode]:
        l = 0
        r = len(nums) - 1
        root = self.build_tree(nums, l, r)
        return root

    def build_tree(self, nums, l, r):
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.build_tree(nums, l, mid - 1)
        root.right = self.build_tree(nums, mid + 1, r)

        return root
