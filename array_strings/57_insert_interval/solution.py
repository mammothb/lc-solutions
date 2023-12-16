from typing import List

import pytest


class Solution:
    def insert(
        self, intervals: List[List[int]], new_interval: List[int]
    ) -> List[List[int]]:
        result = []
        n_intervals = len(intervals)
        i = 0
        while i < n_intervals:
            if intervals[i][1] >= new_interval[0]:
                break
            result.append(intervals[i])
            i += 1
        if i == n_intervals:
            result.append(new_interval)
            return result
        # modify merged interval start
        if intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
        while i < n_intervals:
            if new_interval[1] >= intervals[i][0]:
                new_interval[1] = max(new_interval[1], intervals[i][1])
            else:
                break
            i += 1
        result.append(new_interval)
        while i < n_intervals:
            result.append(intervals[i])
            i += 1

        return result

    def insert_one_loop(
        self, intervals: List[List[int]], new_interval: List[int]
    ) -> List[List[int]]:
        start, stop = new_interval
        result = []
        insert_idx = 0
        for interval in intervals:
            if interval[1] < start:
                result.append(interval)
                insert_idx += 1
            elif interval[0] > stop:
                result.append(interval)
            else:
                start = min(start, interval[0])
                stop = max(stop, interval[1])
        result.insert(insert_idx, [start, stop])
        return result

    def insert_two_loop(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        def is_overlap(interval1, interval2):
            return interval1[1] >= interval2[0]

        result = []
        n = len(intervals)
        i = 0
        while i < n:
            # Break if we reached an element that might overlaps
            if intervals[i][1] >= newInterval[0]:
                break
            result.append(intervals[i])
            i += 1

        result.append(newInterval)
        if i == n:
            return result

        # Merge if current element overlaps. Do this separately
        # because we need to adjust both start and stop
        if is_overlap(result[-1], intervals[i]):
            result[-1][0] = min(result[-1][0], intervals[i][0])
            result[-1][1] = max(result[-1][1], intervals[i][1])
            i += 1

        # Process the rest of the intervals
        while i < n:
            if is_overlap(result[-1], intervals[i]):
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
            i += 1
        return result


@pytest.mark.parametrize(
    "case,expected",
    [
        (([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]]),
        (
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
            [[1, 2], [3, 10], [12, 16]],
        ),
    ],
)
def test_solution(case, expected):
    intervals, new_interval = case
    solution = Solution()
    assert solution.insert(intervals, new_interval) == expected
    assert solution.insert_one_loop(intervals, new_interval) == expected
