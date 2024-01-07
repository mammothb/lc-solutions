# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.result = 0
        self.solve(root, 0, 0)
        return self.result

    def solve(self, root, total, num_nodes):
        if root is None:
            return 0, 0
        l_total, l_nodes = self.solve(root.left, total, num_nodes)
        r_total, r_nodes = self.solve(root.right, total, num_nodes)

        num_nodes += 1 + l_nodes + r_nodes
        total += root.val + l_total + r_total

        if total // num_nodes == root.val:
            self.result += 1
        return total, num_nodes
