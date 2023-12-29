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
