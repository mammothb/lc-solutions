from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        for i in range(len(edges)):
            edges[i].append(i)
        edges = sorted(edges, key=lambda x: x[2])

        critical = []
        pseudo = []
        min_weight = self.kruskal(edges, n)
        for i, (_, _, _, idx) in enumerate(edges):
            if self.kruskal(edges, n, exclude=i) > min_weight:
                critical.append(idx)
            elif self.kruskal(edges, n, include=i) == min_weight:
                pseudo.append(idx)

        return [critical, pseudo]

    def kruskal(self, edges, n, exclude=-1, include=-1):
        parent = {}
        size = {}
        for i in range(n):
            parent[i] = i
            size[i] = 1

        result = 0
        count = 0
        if include != -1:
            result += edges[include][2]
            count += 1
            self.union(parent, size, edges[include][0], edges[include][1])

        for i, (a, b, cost, _) in enumerate(edges):
            if i == exclude:
                continue
            if self.union(parent, size, a, b):
                result += cost
                count += 1
            if count == n - 1:
                break
        if count == n - 1:
            return result
        return float("inf")

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
