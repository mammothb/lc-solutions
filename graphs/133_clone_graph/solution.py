"""
# Definition for a Node.
"""

import collections
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        new_root = Node(node.val)
        queue = collections.deque([node])
        clone_map = {node.val: new_root}
        while queue:
            node = queue.popleft()
            clone_node = clone_map[node.val]
            for neighbor in node.neighbors:
                if neighbor.val not in clone_map:
                    clone_map[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                # Append neighbors as the same nodes which are already
                # cloned instead of creating new neighbors
                clone_node.neighbors.append(clone_map[neighbor.val])

        return new_root

    def cloneGraph_dfs(self, node: Optional["Node"]) -> Optional["Node"]:
        def dfs(node, clone_map):
            if node.val in clone_map:
                return clone_map[node.val]
            new_node = Node(node.val)
            clone_map[node.val] = Node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor, clone_map))
            return new_node

        if node is None:
            return None
        clone_map = {}
        return dfs(node, clone_map)
