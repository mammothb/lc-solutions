"""
Definition of ParentTreeNode:
"""


class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None


class Solution:
    """
    @param node: random node in binary search tree
    @return: the inorder successor of current node
    """

    def inorder_successor(self, node: ParentTreeNode) -> ParentTreeNode:
        # write your code here

        # successor is in the current subtree
        if node.right is not None:
            prev = None
            curr = node.right
            while prev is not None or curr is not None:
                while curr is not None:
                    prev = curr
                    curr = curr.left
                return prev
        # need to traverse up. if parent.right == node, then parent is smaller
        # so we need to traverse higher
        while node.parent is not None and node.parent.right == node:
            node = node.parent
        return node.parent
