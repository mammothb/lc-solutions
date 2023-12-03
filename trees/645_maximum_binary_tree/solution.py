from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def construct_maximum_binary_tree(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(nums, nums_map, start, stop):
            if start >= stop:
                return None
            max_val = max(nums[start:stop])
            max_idx = nums_map[max_val]
            root = TreeNode(max_val)
            root.left = build_tree(nums, nums_map, start, max_idx)
            root.right = build_tree(nums, nums_map, max_idx + 1, stop)
            return root

        nums_map = {num: i for i, num in enumerate(nums)}
        return build_tree(nums, nums_map, 0, len(nums))

    def construct_maximum_binary_tree_iterative(
        self, nums: List[int]
    ) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and node.val > stack[-1].val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
