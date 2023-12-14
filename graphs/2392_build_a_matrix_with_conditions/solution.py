import collections
from typing import List


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def topo_sort(k, conditions):
            graph = collections.defaultdict(list)
            indegree = {}
            for num1, num2 in conditions:
                graph[num1].append(num2)
            for i in range(k):
                num = i + 1
                if num not in indegree:
                    indegree[num] = 0
                for next_num in graph[num]:
                    if next_num in indegree:
                        indegree[next_num] += 1
                    else:
                        indegree[next_num] = 1
            queue = collections.deque()
            result = []
            for i in range(k):
                num = i + 1
                if indegree[num] == 0:
                    queue.append(num)
            while queue:
                num = queue.popleft()
                for next_num in graph[num]:
                    indegree[next_num] -= 1
                    if indegree[next_num] == 0:
                        queue.append(next_num)
                result.append(num)
            if len(result) != k:
                return None
            return result

        row = topo_sort(k, rowConditions)
        col = topo_sort(k, colConditions)
        if row is None or col is None:
            return []
        result = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if row[i] == col[j]:
                    result[i][j] = row[i]
        return result


print(
    Solution().buildMatrix(
        k=3, rowConditions=[[1, 2], [3, 2]], colConditions=[[2, 1], [3, 2]]
    )
)
print(
    Solution().buildMatrix(
        k=3, rowConditions=[[1, 2], [2, 3], [3, 1], [2, 3]], colConditions=[[2, 1]]
    )
)
