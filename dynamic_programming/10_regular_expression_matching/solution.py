class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Cases:
        s[i] == p[j]: dp[i][j] = dp[i-1][j-1]
        p[j] == ".": dp[i][j] = dp[i-1][j-1]
        p[j] == "*":
                dp[i][j] = dp[i-1][j]   * counts multiple
                dp[i][j] = dp[i-1][j-1] * counts as single
                dp[i][j] = dp[i][j-2]   * counts as empty

        p[j-1] doesn't match s[i] and isn't ".", * needs to count as empty:
            dp[i][j] = dp[i][j-2]
        """
        len_s = len(s)
        len_p = len(p)

        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        dp[0][0] = True

        for j in range(1, len_p + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    if p[j - 2] != s[i - 1] and p[j - 2] != ".":
                        dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 1] or dp[i - 1][j] or dp[i][j - 2]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
