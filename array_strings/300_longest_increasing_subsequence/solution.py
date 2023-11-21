from typing import List

import pytest


class Solution:
    def length_of_lis(self, nums: List[int]) -> int:
        n = len(nums)
        result = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    result[i] = max(result[i], result[j] + 1)
        return max(result)

    def length_of_lis_binary_search(self, nums: List[int]) -> int:
        n = len(nums)
        result = [nums[0]]

        for i in range(1, n):
            num = nums[i]
            if num > result[-1]:
                result.append(num)
            else:
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
