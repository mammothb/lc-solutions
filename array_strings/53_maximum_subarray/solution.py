from math import inf
from typing import List

import pytest


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        max_sum = -inf
        curr_sum = 0
        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(curr_sum, 0)
        return int(max_sum)

    def max_sub_array_dp(self, nums: List[int]) -> int:
        # dp[0][i] is max subarray sum up to i (may not include nums[i])
        # dp[1][i] is max subarray sum ending at i (must include nums[i])
        dp = [[0] * len(nums) for _ in range(2)]
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i - 1])
            dp[0][i] = max(dp[0][i - 1], dp[1][i])
        return dp[0][-1]

    def max_sub_array_dac(self, nums: List[int]) -> int:
        def max_sub_array(arr, l, r):
            if l > r:
                return -inf
            mid = (l + r) // 2
            l_sum = 0
            r_sum = 0
            curr_sum = 0
            for i in range(mid - 1, l - 1, -1):
                curr_sum += arr[i]
                l_sum = max(l_sum, curr_sum)
            curr_sum = 0
            for i in range(mid + 1, r + 1):
                curr_sum += arr[i]
                r_sum = max(r_sum, curr_sum)
            return max(
                {
                    max_sub_array(arr, l, mid - 1),
                    max_sub_array(arr, mid + 1, r),
                    l_sum + arr[mid] + r_sum,
                }
            )

        return int(max_sub_array(nums, 0, len(nums) - 1))


@pytest.fixture
def solution():
    return Solution()


def test_sub_array(solution):
    case = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    assert solution.max_sub_array(case) == expected
    assert solution.max_sub_array_dac(case) == expected
    assert solution.max_sub_array_dp(case) == expected


@pytest.mark.parametrize("case,expected", [([1], 1), ([5, 4, -1, 7, 8], 23)])
def test_full_array(solution, case, expected):
    assert solution.max_sub_array(case) == expected
    assert solution.max_sub_array_dac(case) == expected
    assert solution.max_sub_array_dp(case) == expected


def test_negative(solution):
    case = [-2, -3, -1, -5]
    expected = -1
    assert solution.max_sub_array(case) == expected
    assert solution.max_sub_array_dac(case) == expected
    assert solution.max_sub_array_dp(case) == expected
