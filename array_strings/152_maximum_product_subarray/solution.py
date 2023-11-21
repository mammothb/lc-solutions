import sys
from typing import List

import pytest


class Solution:
    def max_product(self, nums: List[int]) -> int:
        max_prod = -sys.maxsize - 1
        curr_prod = 1
        for n in nums:
            curr_prod *= n
            max_prod = max(max_prod, curr_prod)
            if curr_prod == 0:
                curr_prod = 1
        curr_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            curr_prod *= nums[i]
            max_prod = max(max_prod, curr_prod)
            if curr_prod == 0:
                curr_prod = 1
        return max_prod


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("case,expected", [([2, 3, -2, 4], 6), ([-2, 0, -1], 0)])
def test_solution(solution, case, expected):
    assert solution.max_product(case) == expected
