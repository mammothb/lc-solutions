from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]
        memo = {}
        return self.build_tree(1, n, memo)

    def build_tree(self, start, stop, memo):
        if (start, stop) in memo:
            return memo[(start, stop)]
        trees = []
        if start > stop:
            trees.append(None)
            return trees

        for val in range(start, stop + 1):
            left_trees = self.build_tree(start, val - 1, memo)
            right_trees = self.build_tree(val + 1, stop, memo)

            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(val, left_tree, right_tree)
                    trees.append(root)
        memo[(start, stop)] = trees
        return trees
