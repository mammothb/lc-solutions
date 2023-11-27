from typing import List

import pytest


class Solution:
    def erase_overlap_interval(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        result = 0
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] > intervals[i][0]:
                result += 1
                if curr[1] > intervals[i][1]:
                    curr = intervals[i]
            else:
                curr = intervals[i]
        return result

    def erase_overlap_interval_greedy(self, intervals: List[List[int]]) -> int:
        result = 0
        stop = float("-inf")
        for l, r in sorted(intervals, key=lambda x: x[1]):
            # if the start of current interval exceeds end of tracked interval
            # they don't overlap
            if l >= stop:
                stop = r
            else:
                result += 1
        return result


@pytest.mark.parametrize(
    "case,expected",
    [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ],
)
def test_solution(case, expected):
    solution = Solution()
    assert solution.erase_overlap_interval(case) == expected
    assert solution.erase_overlap_interval_greedy(case) == expected
