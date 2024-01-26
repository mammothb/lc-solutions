import heapq
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        costs = [[float("inf")] * nc for _ in range(nr)]
        costs[0][0] = 0

        queue = [(0, 0, 0)]
        while queue:
            cost, i, j = heapq.heappop(queue)

            if i == nr - 1 and j == nc - 1:
                return cost

            if cost > costs[i][j]:
                continue

            for next_i, next_j in (
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1),
            ):
                if not (0 <= next_i < nr and 0 <= next_j < nc):
                    continue
                if grid[next_i][next_j] == 1:
                    next_cost = cost + 1
                else:
                    next_cost = cost
                if next_cost < costs[next_i][next_j]:
                    costs[next_i][next_j] = next_cost
                    heapq.heappush(
                        queue,
                        (costs[next_i][next_j], next_i, next_j),
                    )
