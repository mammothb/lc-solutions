from typing import List

import pytest


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1] * n
        answer = [1] * n

        for i in range(1, n):
            left_prod[i] = nums[i - 1] * left_prod[i - 1]
            j = n - 1 - i
            answer[j] = nums[j + 1] * answer[j + 1]
        for i in range(n):
            answer[i] *= left_prod[i]

        return answer

    def product_except_self_space_optimized(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(1, n):
            answer[i] = nums[i - 1] * answer[i - 1]
        right = 1
        for i in reversed(range(n)):
            answer[i] *= right
            right *= nums[i]

        return answer


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])],
)
def test_solution(solution, case, expected):
    assert solution.product_except_self(case) == expected
    assert solution.product_except_self_space_optimized(case) == expected
