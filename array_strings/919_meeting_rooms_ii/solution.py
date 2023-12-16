import heapq
from typing import List


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        # Write your code here
        intervals = sorted(intervals, key=lambda x: x[0])
        h = []
        result = 0
        for interval in intervals:
            while h and h[0] <= interval[0]:
                heapq.heappop(h)
            heapq.heappush(h, interval[1])
            result = max(result, len(h))
        return result

    def min_meeting_rooms_chronological_ordering(
        self, intervals: List[List[int]]
    ) -> int:
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])

        result = 0
        count = 0
        i_start = 0
        i_end = 0
        # Don't need to care about iterating ends to the finish since
        # we only care about max rooms
        while i_start < len(intervals):
            if starts[i_start] < ends[i_end]:
                count += 1
                i_start += 1
            else:
                count -= 1
                i_end += 1
            result = max(result, count)
        return result
