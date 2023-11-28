import heapq
from typing import List, Tuple

import pytest


def get_median(small, large, k):
    if k % 2 == 1:
        return large[0][0]
    return (large[0][0] - small[0][0]) / 2


def move(src, dst):
    val, idx = heapq.heappop(src)
    heapq.heappush(dst, (-val, idx))


class Solution:
    def median_sliding_window(self, nums: List[int], k: int) -> List[float]:
        small = [(-nums[i], i) for i in range(k)]
        large: List[Tuple[int, int]] = []
        heapq.heapify(small)
        for _ in range((k + 1) // 2):
            move(small, large)

        result = [get_median(small, large, k)]
        for i in range(k, len(nums)):
            # Prioritize keeping the `large` heap bigger
            if nums[i] >= large[0][0]:
                heapq.heappush(large, (nums[i], i))
                # If the element that moved out of the window is smaller than
                # the upper bound of median, shift median up
                if nums[i - k] <= large[0][0]:
                    move(large, small)
            else:
                heapq.heappush(small, (-nums[i], i))
                # If the element that moved out of the window is larger than
                # the upper bound of median, shift median down
                if nums[i - k] >= large[0][0]:
                    move(small, large)
            while small and small[0][1] <= i - k:
                heapq.heappop(small)
            while large and large[0][1] <= i - k:
                heapq.heappop(large)
            result.append(get_median(small, large, k))

        return result


@pytest.mark.parametrize(
    "case,expected",
    [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), [1, -1, -1, 3, 5, 6]),
        (([1, 2, 3, 4, 2, 3, 1, 4, 2], 3), [2, 3, 3, 3, 2, 3, 2]),
        (([1, 2, 3, 4], 4), [2.5]),
    ],
)
def test_solution(case, expected):
    nums, k = case
    solution = Solution()
    actual = solution.median_sliding_window(nums, k)

    assert len(actual) == len(expected)
    assert actual == pytest.approx(expected)
