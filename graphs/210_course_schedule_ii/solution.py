import collections
from typing import DefaultDict, Deque, List

import pytest


class Solution:
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        graph: DefaultDict[int, List[int]] = collections.defaultdict(list)
        indegrees = [0] * num_courses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1

        result = []
        queue: Deque[int] = collections.deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            result.append(course)

            for dependent in graph[course]:
                indegrees[dependent] -= 1
                if indegrees[dependent] == 0:
                    queue.append(dependent)
        return result if len(result) == num_courses else []

    def find_order_dfs(
        self, num_courses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        graph: DefaultDict[int, List[int]] = collections.defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        result: List[int] = []
        visit = [False] * num_courses
        checked = [False] * num_courses
        for course in range(num_courses):
            if not checked[course] and not self.is_acyclic(
                graph, visit, checked, result, course
            ):
                return []
        result.reverse()
        return result

    def is_acyclic(self, graph, visit, checked, result, prereq):
        if visit[prereq]:
            return False
        if checked[prereq]:
            return True
        visit[prereq] = True
        for dependent in graph[prereq]:
            if not self.is_acyclic(graph, visit, checked, result, dependent):
                return False

        visit[prereq] = False
        checked[prereq] = True
        result.append(prereq)
        return True


@pytest.mark.parametrize(
    "case,expected",
    [
        ((2, [[1, 0]]), [[0, 1]]),
        ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [[0, 2, 1, 3], [0, 1, 2, 3]]),
        ((1, []), [[0]]),
    ],
)
def test_solution(case, expected):
    num_courses, prerequisites = case
    solution = Solution()

    assert any(
        solution.find_order(num_courses, prerequisites) == exp for exp in expected
    )
    assert any(
        solution.find_order_dfs(num_courses, prerequisites) == exp for exp in expected
    )
