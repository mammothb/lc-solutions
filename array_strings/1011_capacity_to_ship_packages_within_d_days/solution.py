from typing import List

import pytest


class Solution:
    def ship_within_days(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)
        if days >= len(weights):
            return max(weights)
        min_capacity = max(weights)
        max_capacity = sum(weights)
        while min_capacity < max_capacity:
            mid_capacity = (min_capacity + max_capacity) // 2
            req_days = self.find_shipment_days(weights, mid_capacity)
            if req_days > days:
                min_capacity = mid_capacity + 1
            else:
                max_capacity = mid_capacity
        return min_capacity

    def find_shipment_days(self, weights, capacity):
        days = 1
        curr = 0
        for weight in weights:
            if curr + weight > capacity:
                days += 1
                curr = 0
            curr += weight
        return days


@pytest.mark.parametrize(
    "case,expected",
    [
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15),
        (([3, 2, 2, 4, 1, 4], 3), 6),
    ],
)
def test_solution(case, expected):
    weights, days = case
    solution = Solution()

    assert solution.ship_within_days(weights, days) == expected
