import sys
from typing import List

import pytest


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        memo = {}

        def transaction(prices, day, buy, num_txn):
            if day == len(prices) or num_txn == 2:
                return 0
            key = f"{day}-{buy}-{num_txn}"
            if key in memo:
                return memo[key]
            skip = transaction(prices, day + 1, buy, num_txn)
            if buy:
                no_skip = transaction(prices, day + 1, False, num_txn) - prices[day]
            else:
                no_skip = transaction(prices, day + 1, True, num_txn + 1) + prices[day]
            memo[key] = max(skip, no_skip)
            return memo[key]

        return transaction(prices, 0, True, 0)

    def max_profit_dp(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        # dp[k, i] = profit for k transactions on i-th day
        # dp[k, i] = max(dp[k][i - 1], prices[i] - prices[j] + dp[k - 1][i - 1]),
        # where j = [0, i - 1]
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            low = prices[0]
            for i in range(1, n):
                # if min(low, ...) = low, sell
                low = min(low, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - low)
        return dp[2][n - 1]

    def max_profit_dp_2(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [0] * 3
        mins = [prices[0]] * 3
        for i in range(1, n):
            for k in range(1, 3):
                mins[k] = min(mins[k], prices[i] - dp[k - 1])
                dp[k] = max(dp[k], prices[i] - mins[k])
        return dp[2]

    def max_profit_dp_2_compact(self, prices: List[int]) -> int:
        buy_1 = sys.maxsize + 1
        buy_2 = sys.maxsize + 1
        sell_1 = 0
        sell_2 = 0
        for p in prices:
            buy_1 = min(buy_1, p)
            sell_1 = max(sell_1, p - buy_1)
            buy_2 = min(buy_2, p - sell_1)
            sell_2 = max(sell_2, p - buy_2)

        return sell_2


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        ([3, 3, 5, 0, 0, 3, 1, 4], 6),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_solution(solution, case, expected):
    assert solution.max_profit(case) == expected
    assert solution.max_profit_dp(case) == expected
    assert solution.max_profit_dp_2(case) == expected
    assert solution.max_profit_dp_2_compact(case) == expected
