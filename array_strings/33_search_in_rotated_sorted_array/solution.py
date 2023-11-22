from typing import List

import pytest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, l, r, target):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        # Find the start of the rotated pivot
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        start = l
        if target <= nums[-1]:
            l = start
            r = n - 1
        else:
            l = 0
            r = start - 1
        return binary_search(nums, l, r, target)


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "case,expected",
    [
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1),
        (([1], 0), -1),
    ],
)
def test_solution(solution, case, expected):
    nums, target = case
    assert solution.search(nums, target) == expected
