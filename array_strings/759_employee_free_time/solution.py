from typing import List


class Solution:
    def employee_free_time(self, schedule: List[List[int]]) -> List[List[int]]:
        """
        @param schedule: a list schedule of employees
        @return: Return a list of finite intervals
        """

        # Write your code here
        def is_overlap(interval1, interval2):
            return interval1[1] >= interval2[0]

        schedule = [
            [intervals[i * 2], intervals[i * 2 + 1]]
            for intervals in schedule
            for i in range(len(intervals) // 2)
        ]
        schedule = sorted(schedule, key=lambda x: x[0])
        n = len(schedule)
        result = []
        curr = schedule[0]
        for i in range(1, n):
            if not is_overlap(curr, schedule[i]):
                result.append([curr[1], schedule[i][0]])
                curr = schedule[i]
            elif schedule[i][1] > curr[1]:
                curr = schedule[i]

        return result
