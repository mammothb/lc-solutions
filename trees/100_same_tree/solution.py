from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            return q is None
        if q is None:
            return p is None
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

    def isSameTree_bfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            return q is None
        if q is None:
            return p is None

        queue = collections.deque([p, q])
        while queue:
            p = queue.popleft()
            q = queue.popleft()
            if p.val != q.val:
                return False
            if p.left is not None and q.left is not None:
                queue.append(p.left)
                queue.append(q.left)
            elif p.left is not None or q.left is not None:
                return False
            if p.right is not None and q.right is not None:
                queue.append(p.right)
                queue.append(q.right)
            elif p.right is not None or q.right is not None:
                return False
        return True
