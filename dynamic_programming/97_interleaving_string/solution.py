class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def solve(s1, i, s2, j, s3, k):
            if k == len(s3):
                return True
            left = False
            right = False
            if i < len(s1) and s1[i] == s3[k]:
                left = solve(s1, i + 1, s2, j, s3, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                right = solve(s1, i, s2, j + 1, s3, k + 1)
            return left or right

        if len(s1) + len(s2) != len(s3):
            return False
        return solve(s1, 0, s2, 0, s3, 0)

    def isInterleave_dp(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match_1 = False
                match_2 = False
                if s1[i - 1] == s3[i - 1 + j]:
                    match_1 = dp[i - 1][j]
                if s2[j - 1] == s3[i - 1 + j]:
                    match_2 = dp[i][j - 1]
                dp[i][j] = match_1 or match_2
        return dp[m][n]

    def isInterleave_dp_space_optimized(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] and s2[i - 1] == s3[i - 1]
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                match_1 = False
                match_2 = False
                if s1[i - 1] == s3[i + j - 1]:
                    match_1 = dp[j]
                if s2[j - 1] == s3[i + j - 1]:
                    match_2 = dp[j - 1]
                dp[j] = match_1 or match_2
        return dp[-1]
