from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for t in range(1, amount + 1):
                if t - coin >= 0:
                    dp[t] += dp[t - coin]
        return dp[-1]
