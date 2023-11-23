from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        n = len(prices)
        valley = prices[0]
        peak = prices[0]
        profit = 0
        i = 0
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            profit += peak - valley
        return profit
