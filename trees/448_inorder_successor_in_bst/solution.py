"""
Definition for a binary tree node.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        # write your code here
        stack = []
        found = False
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root == p:
                found = True
            elif found:
                return root
            root = root.right
        return None

    def inorderSuccessor_binary_search(self, root, p):
        result = None
        while root is not None:
            # Keep updating successor value if current node val is larger than p
            if root.val > p.val:
                result = root
                root = root.left
            else:
                root = root.right
        return result
