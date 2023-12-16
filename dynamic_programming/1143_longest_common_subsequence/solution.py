class Solution:
    def longestCommonSubsequence_naive(self, text1: str, text2: str) -> int:
        def solve(text1, i1, n1, text2, i2, n2):
            if i1 == n1 or i2 == n2:
                return 0
            if text1[i1] == text2[i2]:
                length = 1 + solve(text1, i1 + 1, n1, text2, i2 + 1, n2)
            else:
                length = max(
                    solve(text1, i1 + 1, n1, text2, i2, n2),
                    solve(text1, i1, n1, text2, i2 + 1, n2),
                )
            return length

        return solve(text1, 0, len(text1), text2, 0, len(text2))

    def longestCommonSubsequence_memoization(self, text1: str, text2: str) -> int:
        def solve(text1, i1, n1, text2, i2, n2, memo):
            if i1 == n1 or i2 == n2:
                return 0
            if memo[i1][i2] != -1:
                return memo[i1][i2]
            if text1[i1] == text2[i2]:
                length = 1 + solve(text1, i1 + 1, n1, text2, i2 + 1, n2, memo)
            else:
                length = max(
                    solve(text1, i1 + 1, n1, text2, i2, n2, memo),
                    solve(text1, i1, n1, text2, i2 + 1, n2, memo),
                )
            memo[i1][i2] = length
            return length

        memo = [[-1] * len(text2) for _ in text1]
        return solve(text1, 0, len(text1), text2, 0, len(text2), memo)

    def longestCommonSubsequence_bottomup(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1):
            for j in range(len2):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]
