from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        dp = [[float("inf")] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(n - 1):
            for j in range(i + 1):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
                dp[i + 1][j + 1] = min(
                    dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1]
                )

        return min(dp[-1])

    def minimumTotal_optimize_space(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        dp = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]
