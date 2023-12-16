import collections
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # OOM's
        if amount == 0:
            return 0
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        queue = collections.deque()
        for coin in coins:
            queue.append((coin, 0))
        while queue:
            curr_amount, prev_amount = queue.popleft()
            dp[curr_amount] = min(dp[curr_amount], dp[prev_amount] + 1)
            if curr_amount == amount:
                return dp[curr_amount]
            for coin in coins:
                if (
                    curr_amount + coin <= amount
                    and dp[curr_amount] + 1 < dp[curr_amount + coin]
                ):
                    queue.append((curr_amount + coin, curr_amount))
        return -1

    def coinChange_dp(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]
