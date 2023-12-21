import collections
from typing import List

import pytest


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        visited = [False] * n
        if self.is_cyclic(graph, visited, 0, -1):
            return False
        return all(visited)

    def is_cyclic(self, graph, visited, vertex, parent):
        visited[vertex] = True
        for neighbor_vertex in graph[vertex]:
            if (neighbor_vertex != parent and visited[neighbor_vertex]) or (
                not visited[neighbor_vertex]
                and self.is_cyclic(graph, visited, neighbor_vertex, vertex)
            ):
                return True
        return False

    def valid_tree_acyclic(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        checked = [False] * n
        visiting = [False] * n
        # Check for cycle from only 1 starting node
        if not self.is_acyclic(graph, checked, visiting, 0, -1):
            return False
        # Valid tree iff we can reach all nodes
        return all(checked)

    def is_acyclic(self, graph, checked, visiting, vertex, parent):
        if checked[vertex]:
            return True
        if visiting[vertex]:
            return False
        visiting[vertex] = True
        for neighbor_vertex in graph[vertex]:
            if neighbor_vertex == parent or checked[neighbor_vertex]:
                continue
            if visiting[neighbor_vertex] or not self.is_acyclic(
                graph, checked, visiting, neighbor_vertex, vertex
            ):
                return False

        visiting[vertex] = False
        checked[vertex] = True
        return True

    def valid_tree_bfs(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        visited = [False] * n
        queue = collections.deque([(0, -1)])
        while queue:
            vertex, parent = queue.popleft()
            # Cycle detected
            if visited[vertex]:
                return False
            visited[vertex] = True
            for neighbor_vertex in graph[vertex]:
                if neighbor_vertex != parent:
                    queue.append((neighbor_vertex, vertex))
        return all(visited)

    def valid_tree_union_find(self, n: int, edges: List[List[int]]) -> bool:
        def find(parent, vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent, parent[vertex])
            return parent[vertex]

        def union(parent, rank, l_vertex, r_vertex):
            l_rep = find(parent, l_vertex)
            r_rep = find(parent, r_vertex)

            if l_rep == r_rep:
                return False
            if rank[l_rep] < rank[r_rep]:
                l_rep, r_rep = r_rep, l_rep
            parent[l_rep] = r_rep
            rank[l_rep] += 1
            return True

        # need n - 1 edges to connect n vertices
        if len(edges) < n - 1:
            return False

        parent = list(range(n))
        rank = [0] * n
        for l, r in edges:
            if not union(parent, rank, l, r):
                return False
        return True

    def valid_tree_topo_sort_bfs(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        # Edge case, when tree is a single node
        if n == 1 and not edges:
            return True
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            degree[v1] += 1
            degree[v2] += 1
        queue = collections.deque()
        for i in range(n):
            # There are disconnected nodes
            if degree[i] == 0:
                return False
            # Leaf nodes
            if degree[i] == 1:
                queue.append(i)
        while queue:
            vertex = queue.popleft()
            n -= 1
            for neighbor in graph[vertex]:
                if neighbor != vertex:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
        # Check that we can reach all nodes
        return n == 0


@pytest.mark.parametrize(
    "case,expected",
    [
        ((5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True),
        ((5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False),
        ((5, [[0, 2], [0, 3], [1, 4]]), False),
        ((6, [[0, 2], [0, 3], [1, 4], [4, 5], [1, 5]]), False),
    ],
)
def test_solution(case, expected):
    n, edges = case
    solution = Solution()
    assert solution.valid_tree(n, edges) == expected
    assert solution.valid_tree_acyclic(n, edges) == expected
    assert solution.valid_tree_bfs(n, edges) == expected
    assert solution.valid_tree_union_find(n, edges) == expected
