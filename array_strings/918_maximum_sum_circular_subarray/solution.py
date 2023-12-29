from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_total = float("-inf")
        min_total = float("inf")
        total = 0

        max_curr = 0
        min_curr = 0
        for num in nums:
            max_curr += num
            min_curr += num
            total += num
            max_total = max(max_total, max_curr)
            min_total = min(min_total, min_curr)

            if max_curr < 0:
                max_curr = 0
            if min_curr > 0:
                min_curr = 0

        if max_total > 0:
            return max(max_total, total - min_total)
        return max_total
