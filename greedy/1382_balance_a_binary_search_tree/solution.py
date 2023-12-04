# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"T[v: {self.val}, l: {str(self.left)}, r: {str(self.right)}]"


class Solution:
    def balance_bst(self, root: TreeNode) -> TreeNode:
        nodes = []
        stack = []
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            # process
            root = stack.pop()
            nodes.append(root.val)
            root = root.right

        def build_tree(nums, start, stop):
            if start >= stop:
                return None
            mid = (start + stop) // 2
            node = TreeNode(nums[mid])
            node.left = build_tree(nums, start, mid)
            node.right = build_tree(nums, mid + 1, stop)
            return node

        return build_tree(nodes, 0, len(nodes))

    def balance_bst_2(self, root: TreeNode) -> TreeNode:
        nodes = []
        stack = []
        # since input is a BST, when using inorder traversal, the
        # resulting list is already sorted
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root = root.left
            # process
            root = stack.pop()
            nodes.append(root)
            root = root.right

        def build_tree(nodes, start, stop):
            if start >= stop:
                return None
            mid = (start + stop) // 2
            node = nodes[mid]
            node.left = build_tree(nodes, start, mid)
            node.right = build_tree(nodes, mid + 1, stop)
            return node

        return build_tree(nodes, 0, len(nodes))
