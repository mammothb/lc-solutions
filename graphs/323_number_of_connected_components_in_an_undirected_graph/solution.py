import collections
from typing import List


class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """

    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, size, l, r):
            l_rep = find(parent, l)
            r_rep = find(parent, r)
            if l_rep == r_rep:
                return False
            if size[l_rep] < size[r_rep]:
                l_rep, r_rep = r_rep, l_rep
            parent[r_rep] = l_rep
            size[l_rep] += size[r_rep]
            return True

        parent = {i: i for i in range(n)}
        size = {i: 1 for i in range(n)}
        for src, dst in edges:
            if union(parent, size, src, dst):
                n -= 1
        return n

    def count_components_dfs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(graph, visited, i):
            if visited[i]:
                return
            visited[i] = True
            for neighbor in graph[i]:
                if not visited[neighbor]:
                    dfs(graph, visited, neighbor)

        visited = [False] * n
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        result = 0
        for i in range(n):
            if not visited[i]:
                dfs(graph, visited, i)
                result += 1
        return result


print(Solution().count_components(5, [[0, 1], [1, 2], [3, 4]]))
print(Solution().count_components_dfs(5, [[0, 1], [1, 2], [3, 4]]))
