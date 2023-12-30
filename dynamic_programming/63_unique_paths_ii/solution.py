from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nr = len(obstacleGrid)
        nc = len(obstacleGrid[0])

        dp = [[0] * nc for _ in range(nr)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        for i in range(1, nr):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, nc):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, nr):
            for j in range(1, nc):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
