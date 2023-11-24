import collections
from typing import DefaultDict, Deque, List

import pytest


class Solution:
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # Build graph with pre-req as the key
        graph: DefaultDict[int, List[int]] = collections.defaultdict(list)
        for course, prereq in prerequisites:
            if course not in graph[prereq]:
                graph[prereq].append(course)
        visit = [False] * num_courses
        checked = [False] * num_courses
        for prereq in range(num_courses):
            if not checked[prereq] and not self.is_acyclic(
                graph, visit, checked, prereq
            ):
                return False
        return True

    def can_finish_bfs(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        graph: DefaultDict[int, List[int]] = collections.defaultdict(list)
        indegrees = [0] * num_courses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1
        queue: Deque[int] = collections.deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            for dependent in graph[course]:
                indegrees[dependent] -= 1
                if indegrees[dependent] == 0:
                    queue.append(dependent)
        return sum(indegrees) == 0

    def is_acyclic(self, graph, visit, checked, prereq):
        # We're checking a node that's being checked, cycle detected
        if visit[prereq]:
            return False
        # Previously checked acyclic node
        if checked[prereq]:
            return True
        visit[prereq] = True
        for dependent in graph[prereq]:
            if not self.is_acyclic(graph, visit, checked, dependent):
                return False
        checked[prereq] = True
        visit[prereq] = False
        return True


@pytest.mark.parametrize(
    "case,expected", [((2, [[1, 0]]), True), ((2, [[1, 0], [0, 1]]), False)]
)
def test_solution(case, expected):
    num_courses, prerequisites = case
    solution = Solution()
    assert solution.can_finish(num_courses, prerequisites) == expected
    assert solution.can_finish_bfs(num_courses, prerequisites) == expected
