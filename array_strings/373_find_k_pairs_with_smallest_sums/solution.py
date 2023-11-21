import heapq
from typing import List, Tuple

import pytest


class Solution:
    def k_smallest_pairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        result = []
        heap: List[Tuple[int, int]] = []
        len_2 = len(nums2)
        for n in nums1:
            heapq.heappush(heap, (n + nums2[0], 0))
        while k > 0 and heap:
            s, pos = heapq.heappop(heap)
            n2 = nums2[pos]
            n1 = s - n2
            result.append([n1, n2])

            if pos < len_2 - 1:
                pos += 1
                heapq.heappush(heap, (n1 + nums2[pos], pos))
            k -= 1
        return result


@pytest.fixture
def solution():
    return Solution()


def test_solution(solution):
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    expected = [[1, 2], [1, 4], [1, 6]]

    actual = solution.k_smallest_pairs(nums1, nums2, k)

    assert actual == expected


def test_solution_first_repeat(solution):
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    expected = [[1, 1], [1, 1]]

    actual = solution.k_smallest_pairs(nums1, nums2, k)

    assert actual == expected


def test_solution_k_too_big(solution):
    nums1 = [1, 2]
    nums2 = [3]
    k = 3
    expected = [[1, 3], [2, 3]]

    actual = solution.k_smallest_pairs(nums1, nums2, k)

    assert actual == expected
