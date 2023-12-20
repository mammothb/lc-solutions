import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = collections.defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)

        queue = collections.deque()
        for v in range(n):
            if len(graph[v]) == 1:
                queue.append(v)

        while n > 2:
            n_leaves = len(queue)
            n -= n_leaves
            for _ in range(n_leaves):
                v = queue.popleft()
                for neighbor_v in graph[v]:
                    graph[neighbor_v].remove(v)
                    if len(graph[neighbor_v]) == 1:
                        queue.append(neighbor_v)
                del graph[v]
        return list(queue)
