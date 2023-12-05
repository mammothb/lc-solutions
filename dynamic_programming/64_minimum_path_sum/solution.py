from typing import List


class Solution:
    def minPathSum_brute_force(self, grid: List[List[int]]) -> int:
        def solve(grid, nr, nc, i, j, curr, result):
            curr += grid[i][j]
            if i == nr - 1 and j == nc - 1:
                result.append(curr)
            if i < nr - 1:
                solve(grid, nr, nc, i + 1, j, curr, result)
            if j < nc - 1:
                solve(grid, nr, nc, i, j + 1, curr, result)

        result = []
        solve(grid, len(grid), len(grid[0]), 0, 0, 0, result)
        return min(result)

    def minPathSum_dp(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        for i in range(1, nr):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, nc):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, nr):
            for j in range(1, nc):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
