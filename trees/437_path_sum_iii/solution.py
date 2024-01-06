import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def solve(node, target, res):
            if node is None:
                return

            add(node, target, res)
            solve(node.left, target, res)
            solve(node.right, target, res)

        def add(node, target, res):
            if node is None:
                return
            if node.val == target:
                res[0] += 1
            if node.left is not None:
                add(node.left, target - node.val, res)
            if node.right is not None:
                add(node.right, target - node.val, res)

        if root is None:
            return 0

        res = [0]
        solve(root, targetSum, res)
        return res[0]

    def pathSum_cache(self, root: Optional[TreeNode], targetSum: int) -> int:
        def solve(node, target, curr, res, cache):
            if node is None:
                return
            curr += node.val
            diff = curr - target
            if diff in cache:
                res[0] += cache[diff]
            if curr in cache:
                cache[curr] += 1
            else:
                cache[curr] = 1
            solve(node.left, target, curr, res, cache)
            solve(node.right, target, curr, res, cache)
            cache[curr] -= 1

        res = [0]
        cache = {0: 1}
        solve(root, targetSum, 0, res, cache)

        return res[0]

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        cache = collections.defaultdict(int)
        cache[0] = 1
        self.solve(root, targetSum, 0, cache)

        return self.result

    def solve(self, root, targetSum, curr, cache):
        if root is None:
            return

        curr += root.val
        self.result += cache[curr - targetSum]

        cache[curr] += 1
        if root.left is not None:
            self.solve(root.left, targetSum, curr, cache)
        if root.right is not None:
            self.solve(root.right, targetSum, curr, cache)
        cache[curr] -= 1
