from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def solve(node, target, result, curr):
            target -= node.val
            if target == 0 and node.left is None and node.right is None:
                result.append(curr + [node.val])
                return

            if node.left is not None:
                solve(
                    node.left,
                    target,
                    result,
                    curr + [node.val],
                )
            if node.right is not None:
                solve(
                    node.right,
                    target,
                    result,
                    curr + [node.val],
                )

        result = []
        if root is None:
            return result

        solve(root, targetSum, result, [])
        return result

    def pathSum_2(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def solve(node, target, result, curr):
            if target == 0 and node.left is None and node.right is None:
                result.append(curr)
                return

            if node.left is not None:
                solve(node.left, target - node.left.val, result, curr + [node.left.val])
            if node.right is not None:
                solve(
                    node.right, target - node.right.val, result, curr + [node.right.val]
                )

        result = []
        if root is None:
            return result

        solve(root, targetSum - root.val, result, [root.val])
        return result
