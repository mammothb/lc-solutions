import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, nr, nc, i, j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ii < nr and 0 <= jj < nc and grid[ii][jj] != "0":
                    dfs(grid, nr, nc, ii, jj)

        result = 0
        nr = len(grid)
        nc = len(grid[0])
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] != "0":
                    dfs(grid, nr, nc, i, j)
                    result += 1
        return result

    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        def bfs(grid, nr, nc, i, j):
            queue = collections.deque([(i, j)])
            while queue:
                i, j = queue.popleft()
                for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= ii < nr and 0 <= jj < nc and grid[ii][jj] != "0":
                        grid[ii][jj] = "0"
                        queue.append((ii, jj))

        result = 0
        nr = len(grid)
        nc = len(grid[0])
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] != "0":
                    grid[i][j] = "0"
                    bfs(grid, nr, nc, i, j)
                    result += 1
        return result

    def numIslands_union_find(self, grid: List[List[str]]) -> int:
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, rank, l, r):
            l_rep = find(parent, l)
            r_rep = find(parent, r)
            if l_rep == r_rep:
                return
            if rank[l_rep] < rank[r_rep]:
                l_rep, r_rep = r_rep, l_rep
            parent[r_rep] = l_rep
            if rank[l_rep] == rank[r_rep]:
                rank[l_rep] += 1
            self.count -= 1

        nr = len(grid)
        nc = len(grid[0])

        self.count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    self.count += 1
        parent = {i: i for i in range(nr * nc)}
        rank = {i: 0 for i in range(nr * nc)}
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "0":
                    continue
                idx = i * nc + j
                if j < nc - 1 and grid[i][j + 1] == "1":
                    union(parent, rank, idx, idx + 1)
                if i < nr - 1 and grid[i + 1][j] == "1":
                    union(parent, rank, idx, idx + nc)
        return self.count
