from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_equal(root1, root2):
            if root1 is None or root2 is None:
                return root1 == root2
            return (
                root1.val == root2.val
                and is_equal(root1.left, root2.left)
                and is_equal(root1.right, root2.right)
            )

        def solve(root, sub_root):
            if root is None:
                return False
            return (
                is_equal(root, sub_root)
                or solve(root.left, sub_root)
                or solve(root.right, sub_root)
            )

        return solve(root, subRoot)

    def isSubtree_serialize(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        # If you serialize preorder traversal and include null nodes, you
        # get a unique representation
        def serialize(node):
            result = ""
            stack = [node]
            while stack:
                node = stack.pop()
                if node is None:
                    result += ",#"
                else:
                    result += f",{node.val}"
                    stack.append(node.right)
                    stack.append(node.left)
            return result

        root_string = serialize(root)
        sub_root_string = serialize(subRoot)
        return sub_root_string in root_string
