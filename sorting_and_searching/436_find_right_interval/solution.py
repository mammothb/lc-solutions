from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index = {(interval[0], interval[1]): i for i, interval in enumerate(intervals)}
        n = len(intervals)
        result = [-1] * n
        intervals = sorted(intervals)
        for interval in intervals:
            src_idx = index[tuple(interval)]
            l = 0
            r = n - 1
            idx = -1
            while l <= r:
                mid = l + (r - l) // 2
                if self.is_right(interval, intervals[mid]):
                    idx = mid
                if intervals[mid][0] < interval[1]:
                    l = mid + 1
                else:
                    r = mid - 1
            if idx != -1:
                result[src_idx] = index[tuple(intervals[idx])]
        return result

    def is_right(self, interval1, interval2):
        return interval2[0] >= interval1[1]
