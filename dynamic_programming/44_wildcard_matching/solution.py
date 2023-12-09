class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_p = len(p)
        len_s = len(s)

        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        dp[-1][-1] = True

        for j in range(len_p - 1, -1, -1):
            if p[j] != "*":
                break
            dp[-1][j] = True

        for i in range(len_s - 1, -1, -1):
            for j in range(len_p - 1, -1, -1):
                if s[i] == p[j] or p[j] == "?":
                    dp[i][j] = dp[i + 1][j + 1]
                elif p[j] == "*":
                    dp[i][j] = dp[i + 1][j] or dp[i][j + 1]
                else:
                    dp[i][j] = False
        return dp[0][0]
