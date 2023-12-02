from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.root = root

    def next(self) -> int:
        while self.root is not None:
            self.stack.append(self.root)
            self.root = self.root.left
        self.root = self.stack.pop()
        result = self.root.val
        self.root = self.root.right
        return result

    def hasNext(self) -> bool:
        return self.root is not None or bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
