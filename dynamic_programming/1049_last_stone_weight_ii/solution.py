from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Want to split the stones in piles that is as close to half the total
        # weight as possible
        stones = sorted(stones)
        n = len(stones)
        total = sum(stones)
        target = total // 2

        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for t in range(1, target + 1):
            for i in range(n):
                if t - stones[i] >= 0:
                    dp[i + 1][t] = max(dp[i][t], dp[i][t - stones[i]] + stones[i])
                else:
                    dp[i + 1][t] = dp[i][t]
        return total - 2 * dp[-1][-1]
