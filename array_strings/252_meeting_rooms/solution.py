from typing import List


class Solution:
    def attend_meeting(self, intervals: List[List[int]]) -> bool:
        def is_overlap(interval1, interval2):
            return interval1[1] > interval2[0]

        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if is_overlap(intervals[i], intervals[i + 1]):
                return False
        return True


print(Solution().attend_meeting([[0, 30], [5, 10], [15, 20]]))
print(Solution().attend_meeting([[7, 10], [2, 4]]))
