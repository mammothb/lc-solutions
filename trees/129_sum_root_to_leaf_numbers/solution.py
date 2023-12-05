from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def get_number(node, number, result):
            if node.left is None and node.right is None:
                result.append(number * 10 + node.val)
            if node.left is not None:
                get_number(node.left, number * 10 + node.val, result)
            if node.right is not None:
                get_number(node.right, number * 10 + node.val, result)

        result = []
        get_number(root, 0, result)
        return sum(result)

    def sumNumbers_2(self, root: Optional[TreeNode]) -> int:
        def dfs(node, number):
            if node is None:
                return 0
            curr = number * 10 + node.val
            if node.left is None and node.right is None:
                return curr
            return dfs(node.left, curr) + dfs(node.right, curr)

        return dfs(root, 0)

    def sumNumbers_iterative_dfs(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        result = 0
        while stack:
            node, number = stack.pop()
            curr = number * 10 + node.val
            if node.left is None and node.right is None:
                result += curr
            if node.left is not None:
                stack.append((node.left, curr))
            if node.right is not None:
                stack.append((node.right, curr))
        return result
