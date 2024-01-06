import collections
from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        def solve(graph, seen, start, target, curr, result):
            if start not in graph:
                return False
            if start == target:
                result.append(curr)
                return True

            seen.add(start)
            for num, val in graph[start]:
                if num not in seen and solve(
                    graph, seen, num, target, curr * val, result
                ):
                    return True
            seen.remove(start)

            return False

        n = len(equations)
        graph = collections.defaultdict(list)

        for i in range(n):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1.0 / values[i]))

        result = []
        for num1, num2 in queries:
            if not solve(graph, set(), num1, num2, 1.0, result):
                result.append(-1.0)
        return result

    def calcEquation2(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        graph = collections.defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        result = []
        for start, stop in queries:
            _, val = self.solve(graph, set(), start, stop, 1.0)
            result.append(val)
        return result

    def solve(self, graph, seen, start, stop, curr):
        if start not in graph or stop not in graph:
            return False, -1.0
        if start == stop:
            return True, curr

        seen.add(start)
        for next, val in graph[start]:
            if next in seen:
                continue
            rc, result = self.solve(graph, seen, next, stop, curr * val)
            if rc:
                return True, result
        seen.remove(start)
        return False, -1.0


print(
    Solution().calcEquation2(
        equations=[["a", "b"], ["b", "c"]],
        values=[2.0, 3.0],
        queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    )
)
