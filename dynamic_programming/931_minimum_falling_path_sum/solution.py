from typing import List


class Solution:
    # def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    #     self.result = float("inf")
    #     n = len(matrix)
    #     for j in range(n):
    #         self.solve(matrix, n, 0, j, 0)
    #     return self.result

    # def solve(self, matrix, n, i, j, curr):
    #     if i == n:
    #         self.result = min(self.result, curr)
    #         return

    #     curr += matrix[i][j]
    #     for next_j in (j - 1, j, j + 1):
    #         if 0 <= next_j < n:
    #             self.solve(matrix, n, i + 1, next_j, curr)

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float("inf")] * n for _ in range(n)]
        for j in range(n):
            dp[-1][j] = matrix[-1][j]

        for i in range(n - 2, -1, -1):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(
                    dp[i + 1][j - 1] if 0 <= j - 1 else float("inf"),
                    dp[i + 1][j],
                    dp[i + 1][j + 1] if j + 1 < n else float("inf"),
                )
        return min(dp[0])
