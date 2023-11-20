from typing import List

import pytest


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j != k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    prev_lo = nums[j]
                    prev_hi = nums[k]
                    while j < k and nums[j] == prev_lo:
                        j += 1
                    while j < k and nums[k] == prev_hi:
                        k -= 1
        return result


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_solution(solution, case, expected):
    actual = solution.three_sum(case)
    assert actual == expected
