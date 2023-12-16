import sys
from typing import List

import pytest


class Solution:
    def length_of_lis(self, nums: List[int]) -> int:
        n = len(nums)
        result = [1] * n
        for stop in range(1, n):
            for i in range(stop):
                if nums[i] < nums[stop]:
                    # update result at nums[stop] if nums[i] is smaller and its
                    # subsequence is longer
                    result[stop] = max(result[stop], result[i] + 1)
        return max(result)

    def length_of_lis_brute_force(self, nums: List[int]) -> int:
        def solve(nums, start, prev):
            if start >= len(nums):
                return 0
            skip = solve(nums, start + 1, prev)
            if nums[start] > prev:
                no_skip = 1 + solve(nums, start + 1, nums[start])
            else:
                no_skip = 0
            return max(skip, no_skip)

        return solve(nums, 0, -sys.maxsize - 1)

    def length_of_lis_binary_search(self, nums: List[int]) -> int:
        n = len(nums)
        result = [nums[0]]

        for i in range(1, n):
            num = nums[i]
            if num > result[-1]:
                result.append(num)
            else:
                # Start a new subsequence by overwriting the current one
                l = 0
                r = len(result) - 1
                idx = 0
                while l <= r:
                    mid = (l + r) // 2
                    if result[mid] == num:
                        idx = mid
                        break
                    elif result[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid - 1
                        # Overwrite the smallest element that's larger than
                        # nums[i]
                        idx = mid
                result[idx] = nums[i]
        return len(result)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([10, 9, 2, 5, 3, 4], 3),
    ],
)
def test_solution(solution, case, expected):
    assert solution.length_of_lis(case) == expected
    assert solution.length_of_lis_binary_search(case) == expected


def test_duplicate(solution):
    case = [7, 7, 7, 7, 7, 7, 7]
    expected = 1
    assert solution.length_of_lis(case) == expected
    assert solution.length_of_lis_binary_search(case) == expected
