import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Prim's algorithm"""
        n = len(points)
        visited = [False] * n
        costs = {0: 0}
        h = [(0, 0)]
        result = 0
        while h:
            cost, v = heapq.heappop(h)
            if visited[v] or (v in costs and costs[v] < cost):
                continue

            visited[v] = True
            result += cost

            for next_v in range(n):
                if visited[next_v]:
                    continue
                cost = self.manhattan_distance(points[v], points[next_v])
                if next_v not in costs or costs[next_v] > cost:
                    costs[next_v] = cost
                    heapq.heappush(h, (cost, next_v))

        return result

    def minCostConnectPoints2(self, points: List[List[int]]) -> int:
        """Kruskal's algorithm"""
        n = len(points)
        parent = {}
        size = {}
        h = []
        for i in range(n):
            parent[i] = i
            size[i] = 1
            for j in range(i + 1, n):
                h.append((self.manhattan_distance(points[i], points[j]), i, j))
        heapq.heapify(h)

        result = 0
        num_edge = 0
        while num_edge < n - 1 and h:
            cost, i, j = heapq.heappop(h)
            if self.union(parent, size, i, j):
                result += cost
                num_edge += 1
        return result

    def manhattan_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, size, l, r):
        l_rep = self.find(parent, l)
        r_rep = self.find(parent, r)

        if l_rep == r_rep:
            return False

        if size[l_rep] < size[r_rep]:
            l_rep, r_rep = r_rep, l_rep
        parent[r_rep] = l_rep
        size[l_rep] += size[r_rep]

        return True
