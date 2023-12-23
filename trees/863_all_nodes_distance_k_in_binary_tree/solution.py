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

    def distanceK_bfs_2(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def connect(graph, parent, child):
            if parent is not None:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            if child.left is not None:
                connect(graph, child, child.left)
            if child.right is not None:
                connect(graph, child, child.right)

        graph = collections.defaultdict(list)
        connect(graph, None, root)

        result = []
        seen = set()
        queue = collections.deque([(target.val, 0)])
        while queue:
            node, step = queue.popleft()
            seen.add(node)
            if step == k:
                result.append(node)
                continue

            for next_node in graph[node]:
                if next_node not in seen:
                    queue.append((next_node, step + 1))
        return result

    def distance_k_non_graph(
        self, root: TreeNode, target: TreeNode, k: int
    ) -> List[int]:
        # Create a map of distances from root to target so they can be used
        # as the starting distance when traversing from target back up to other
        # nodes
        def find(dist, parent, target):
            if parent is None:
                return -1
            if parent.val == target.val:
                dist[parent.val] = 0
                return dist[parent.val]
            left = find(dist, parent.left, target)
            if left != -1:
                dist[parent.val] = left + 1
                return dist[parent.val]
            right = find(dist, parent.right, target)
            if right != -1:
                dist[parent.val] = right + 1
                return dist[parent.val]
            return -1

        def dfs(dist, parent, target, k, distance, result):
            if parent is None:
                return
            if parent.val in dist:
                distance = dist[parent.val]
            if distance == k:
                result.append(parent.val)
            dfs(dist, parent.left, target, k, distance + 1, result)
            dfs(dist, parent.right, target, k, distance + 1, result)

        dist = {}
        find(dist, root, target.val)

        result = []
        dfs(dist, root, target, k, dist[root.val], result)

        return result
