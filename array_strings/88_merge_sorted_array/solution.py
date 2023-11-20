from typing import List

import pytest


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        idx_m = m - 1
        idx_n = n - 1
        idx_merge = m + n - 1

        while idx_n >= 0:
            if idx_m < 0 or nums2[idx_n] >= nums1[idx_m]:
                nums1[idx_merge] = nums2[idx_n]
                idx_n -= 1
                idx_merge -= 1
            else:
                nums1[idx_merge] = nums1[idx_m]
                idx_m -= 1
                idx_merge -= 1


@pytest.fixture
def solution():
    return Solution()


def test_normal(solution):
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]

    solution.merge(nums1, m, nums2, n)

    assert nums1 == expected


def test_right_empty(solution):
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    expected = [1]

    solution.merge(nums1, m, nums2, n)

    assert nums1 == expected


def test_right_empty(solution):
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    expected = [1]

    solution.merge(nums1, m, nums2, n)

    assert nums1 == expected
