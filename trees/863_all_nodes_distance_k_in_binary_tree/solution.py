import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distance_k(self, root: treenode, target: treenode, k: int) -> list[int]:
        graph = collections.defaultdict(list)

        def connect(parent, child):
            if parent is not None and child is not None:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            if child.left is not None:
                connect(child, child.left)
            if child.right is not None:
                connect(child, child.right)

        connect(None, root)

        result = [target.val]
        seen = set(result)
        # BFS traversal
        for _ in range(k):
            new_level = []
            for node in result:
                for conn_node in graph[node]:
                    if conn_node not in seen:
                        new_level.append(conn_node)
                        seen.add(conn_node)
            result = new_level
        return result

    def distance_k_non_graph(
        self, root: TreeNode, target: TreeNode, k: int
    ) -> List[int]:
        dist = {}

        # Create a map of distances from root to target so they can be used
        # as the starting distance when traversing from target back up to other
        # nodes
        def find(parent, target_val):
            if parent is None:
                return -1
            if parent.val == target_val:
                dist[parent.val] = 0
                return 0
            left = find(parent.left, target_val)
            if left != -1:
                dist[parent.val] = left + 1
                return left + 1
            right = find(parent.right, target_val)
            if right != -1:
                dist[parent.val] = right + 1
                return right + 1

        find(root, target.val)
        result = []

        def dfs(parent, target_val, k, distance, result):
            if parent is None:
                return
            if parent.val in dist:
                distance = dist[parent.val]
            if distance == k:
                result.append(parent.val)
            dfs(parent.left, target_val, k, distance + 1, result)
            dfs(parent.right, target_val, k, distance + 1, result)

        dfs(root, target.val, k, dist[root.val], result)
        return result
