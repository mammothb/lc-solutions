import collections
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        size = {}
        num_edge = {}
        for i in range(n):
            parent[i] = i
            size[i] = 1
            num_edge[i] = 0
        for u, v in edges:
            self.union(parent, size, num_edge, u, v)
        seen = set()
        result = 0
        for i in range(n):
            idx = self.find(parent, i)
            if idx in seen:
                continue
            seen.add(idx)

            if num_edge[idx] == (size[idx] * (size[idx] - 1)) // 2:
                result += 1

        return result

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, size, num_edge, l, r):
        l_rep = self.find(parent, l)
        r_rep = self.find(parent, r)
        if size[l_rep] < size[r_rep]:
            l_rep, r_rep = r_rep, l_rep

        num_edge[l_rep] += 1

        if l_rep == r_rep:
            return

        parent[r_rep] = l_rep
        size[l_rep] += size[r_rep]
        n_edge = num_edge[l_rep] + num_edge[r_rep]
        num_edge[l_rep] = n_edge
        num_edge[r_rep] = n_edge

    def countCompleteComponents2(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit = [False] * n
        result = 0
        for i in range(n):
            if visit[i]:
                continue
            num_nodes, num_edges = self.dfs(graph, visit, i, 0, 0)
            if num_edges == (num_nodes * (num_nodes - 1)):
                result += 1
        return result

    def dfs(self, graph, visit, node, num_nodes, num_edges):
        if visit[node]:
            return num_nodes, num_edges
        visit[node] = True
        num_nodes += 1
        num_edges += len(graph[node])
        for next_node in graph[node]:
            num_nodes, num_edges = self.dfs(
                graph, visit, next_node, num_nodes, num_edges
            )
        return num_nodes, num_edges
