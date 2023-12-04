import collections
from typing import List


class Solution:
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent, parent[vertex])
            return parent[vertex]

        def union(parent, rank, l_vertex, r_vertex):
            l_rep = find(parent, l_vertex)
            r_rep = find(parent, r_vertex)

            # If there is a cycle, the two vertices are already under the same parent
            if l_rep == r_rep:
                return True
            if rank[l_rep] < rank[r_rep]:
                l_rep, r_rep = r_rep, l_rep
            parent[r_rep] = l_rep
            if rank[l_rep] == rank[r_rep]:
                rank[l_rep] += 1
            return False

        parent = {i + 1: i + 1 for i in range(len(edges))}
        rank = {i + 1: 0 for i in range(len(edges))}
        for v1, v2 in edges:
            if union(parent, rank, v1, v2):
                return [v1, v2]

    def find_redundant_connection_dfs(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            visited = set()
            graph[v1].append(v2)
            graph[v2].append(v1)
            # If graph becomes cylic after the current edge, return it
            if self.is_cyclic(graph, visited, v1, -1):
                return [v1, v2]

    def is_cyclic(self, graph, visited, vertex, parent):
        if vertex in visited:
            return True
        visited.add(vertex)
        if vertex not in graph:
            return False
        for neighbor_vertex in graph[vertex]:
            if neighbor_vertex != parent and self.is_cyclic(
                graph, visited, neighbor_vertex, vertex
            ):
                return True
        return False

    def find_redundant_connection_bfs(self, edges: List[List[int]]) -> List[int]:
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            indegree[v1] += 1
            indegree[v2] += 1

        queue = collections.deque(
            [vertex for vertex, degree in indegree.items() if degree == 1]
        )
        while queue:
            vertex = queue.popleft()
            indegree[vertex] -= 1
            for neighbor_vertex in graph[vertex]:
                indegree[neighbor_vertex] -= 1
                if indegree[neighbor_vertex] == 1:
                    queue.append(neighbor_vertex)

        for v1, v2 in reversed(edges):
            if indegree[v1] == 2 and indegree[v2] == 2:
                return [v1, v2]
