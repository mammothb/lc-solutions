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

    def findOrder_dfs_2(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        def is_acyclic(graph, checked, visit, course, result):
            if visit[course]:
                return False
            if checked[course]:
                return True
            visit[course] = True
            for next_course in graph[course]:
                if checked[next_course]:
                    continue
                if visit[next_course] or not is_acyclic(
                    graph, checked, visit, next_course, result
                ):
                    return False
            visit[course] = False
            checked[course] = True
            result.append(course)
            return True

        graph = collections.defaultdict(list)
        # Construct graph with course and its prerequisites as the
        # adjacency list. So when we do DFS later, the first course added
        # will be one without any other prerequisites.
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        checked = [False] * numCourses
        visit = [False] * numCourses
        result = []
        for course in range(numCourses):
            if checked[course]:
                continue
            if not is_acyclic(graph, checked, visit, course, result):
                return []
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
