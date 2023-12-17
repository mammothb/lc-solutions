class Solution:
    def num_decodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # Behaves like fib if all chars can be alone
        # skip once if char exceeds 26, skip twice if char is 0
        for i in range(2, n + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6"):
                dp[i] += dp[i - 2]
        return dp[n]

    def numDecodings_alt(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]
            # If the current char and prev char can form a valid number <= 26
            if s[i - 2] != "0" and int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]

    def num_decodings_bottom_up(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] != "0":
                dp[i] += dp[i + 1]
            if i < n - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6")):
                dp[i] += dp[i + 2]
        return dp[0]
