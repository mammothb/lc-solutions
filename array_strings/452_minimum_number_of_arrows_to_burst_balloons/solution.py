from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def is_overlap(interval1, interval2):
            return interval1[1] >= interval2[0]

        points = sorted(points, key=lambda x: x[0])
        result = 1
        curr_interval = points[0]
        n = len(points)
        for i in range(1, n):
            if is_overlap(curr_interval, points[i]):
                if curr_interval[1] > points[i][1]:
                    curr_interval = points[i]
            else:
                curr_interval = points[i]
                result += 1
        return result
