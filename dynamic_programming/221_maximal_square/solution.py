from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nr = len(matrix)
        nc = len(matrix[0])

        dp = [[0] * nc for _ in range(nr)]
        result = 0
        for i in range(nr):
            dp[i][0] = int(matrix[i][0])
            result = max(result, dp[i][0])
        for j in range(nc):
            dp[0][j] = int(matrix[0][j])
            result = max(result, dp[0][j])

        for i in range(1, nr):
            for j in range(1, nc):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                result = max(result, dp[i][j])
        return result**2
