from typing import List

import pytest


class Solution:
    def sort_colors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lo = 0
        hi = n - 1
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        for i in reversed(range(n)):
            if nums[i] == 2:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1

    def sort_colors_dnf(self, nums: List[int]) -> None:
        n = len(nums)
        lo = 0
        hi = n - 1
        i = 0
        while i <= hi:
            if nums[i] == 0:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
            else:
                i += 1


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([2, 0, 2], [0, 2, 2]),
    ],
)
def test_solution(solution, case, expected):
    case_copy = case.copy()
    solution.sort_colors(case_copy)
    assert case_copy == expected

    case_copy = case.copy()
    solution.sort_colors_dnf(case_copy)
    assert case_copy == expected
