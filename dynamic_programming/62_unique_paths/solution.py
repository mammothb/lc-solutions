class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        start tracking at [1, 1]
        2, 3, 4
        3, 6, 10
        """
        if m == 1 or n == 1:
            return 1
        dp = [2 + i for i in range(m - 1)]
        for i in range(3, n + 1):
            for j in range(m - 1):
                if j == 0:
                    dp[j] = i
                else:
                    dp[j] += dp[j - 1]
        return dp[-1]

    def uniquePaths_2(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(1, n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePaths_3(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            dp[0] = 1
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
