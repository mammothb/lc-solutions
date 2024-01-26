import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        costs = [[float("inf")] * nc for _ in range(nr)]
        costs[0][0] = grid[0][0]

        h = [(costs[0][0], 0, 0)]
        while h:
            cost, i, j = heapq.heappop(h)
            if cost > costs[i][j]:
                continue
            if i == nr - 1 and j == nc - 1:
                return cost

            for next_i, next_j in (
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ):
                if not (0 <= next_i < nr and 0 <= next_j < nc):
                    continue
                next_cost = max(cost, grid[next_i][next_j])
                if next_cost < costs[next_i][next_j]:
                    costs[next_i][next_j] = next_cost
                    heapq.heappush(h, (next_cost, next_i, next_j))
        return -1
