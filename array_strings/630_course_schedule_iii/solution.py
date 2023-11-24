import heapq
import operator
from typing import List

import pytest


class Solution:
    def schedule_course(self, courses: List[List[int]]) -> int:
        # sort by end date so the cumulative duration of the courses taken
        courses = sorted(courses, key=operator.itemgetter(1))
        h: List[int] = []
        curr_day = 0
        for course in courses:
            curr_day += course[0]
            heapq.heappush(h, -course[0])
            # if the cumulative days exceed the current course's deadline
            # remove a taken course with the longest duration, either the
            # current course (skip) or one of the previously taken course
            # which frees up more time
            if curr_day > course[1]:
                curr_day += heapq.heappop(h)
        return len(h)

    def schedule_course_2(self, courses: List[List[int]]) -> int:
        # sort by end date so the cumulative duration of the courses taken
        courses = sorted(courses, key=operator.itemgetter(1))
        h: List[int] = []
        curr_day = 0
        for course in courses:
            # Can take course
            if curr_day + course[0] <= course[1]:
                curr_day += course[0]
                heapq.heappush(h, -course[0])
            # Can't take, but have taken a course with longer duration
            elif h and h[0] < -course[0]:
                curr_day += heapq.heappop(h) + course[0]
                heapq.heappush(h, -course[0])
        return len(h)


@pytest.mark.parametrize(
    "case,expected",
    [
        ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
        ([[1, 2]], 1),
        ([[3, 2], [4, 3]], 0),
    ],
)
def test_solution(case, expected):
    solution = Solution()
    assert solution.schedule_course(case) == expected
    assert solution.schedule_course_2(case) == expected
