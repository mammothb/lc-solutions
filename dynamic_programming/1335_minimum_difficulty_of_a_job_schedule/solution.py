from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        def dfs(jobs, d):
            if d == 1:
                return max(jobs)

            min_difficulty = float("inf")
            for i in range(1, len(jobs)):
                min_difficulty = min(
                    min_difficulty,
                    max(jobs[:i]) + dfs(jobs[i:], d - 1),
                )
            return min_difficulty

        result = dfs(jobDifficulty, d)
        if result == float("inf"):
            return -1
        return result

    def minDifficulty_dp(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1

        dp = [[float("inf")] * d for _ in range(n)]
        dp[0][0] = jobDifficulty[0][0]
        # Set up max(a), max(a,b) etc
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1], jobDifficulty[i])

        for i in range(1, n):
            for j in range(1, min(i + 1, d)):
                for k in range(i):
                    # compute min of curr with
                    # earlier row and max of rest of the job up to row
                    dp[i][j] = min(
                        dp[i][j], dp[k][j - 1] + max(jobDifficulty[k + 1 : i + 1])
                    )
        return dp[-1][-1]

    def minDifficulty_dp_2(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [[float("inf")] * (n + 1) for _ in range(d + 1)]
        for i in range(d + 1):
            dp[i][-1] = 0

        for day in range(1, d + 1):
            for i in range(n - day + 1):
                max_difficulty = 0
                for j in range(i, n - day + 1):
                    max_difficulty = max(max_difficulty, jobDifficulty[j])
                    dp[day][i] = min(dp[day][i], max_difficulty + dp[day - 1][j + 1])
        if dp[-1][0] == float("inf"):
            return -1
        return dp[-1][0]
