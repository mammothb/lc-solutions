from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for p in prices[1:]:
            if p < lowest:
                lowest = p
            else:
                profit = max(profit, p - lowest)
        return profit
