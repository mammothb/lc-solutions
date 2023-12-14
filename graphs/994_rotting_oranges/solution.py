import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        result = 0
        num_fresh = 0
        queue = collections.deque()
        seen = set()
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    seen.add((i, j))
                elif grid[i][j] == 1:
                    num_fresh += 1
        while queue:
            n_nodes = len(queue)
            for _ in range(n_nodes):
                i, j = queue.popleft()
                grid[i][j] = 2
                for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if (
                        0 <= ii < nr
                        and 0 <= jj < nc
                        and grid[ii][jj] == 1
                        and (ii, jj) not in seen
                    ):
                        seen.add((ii, jj))
                        queue.append((ii, jj))
                        num_fresh -= 1
            if queue:
                result += 1
        if num_fresh > 0:
            return -1
        return result
