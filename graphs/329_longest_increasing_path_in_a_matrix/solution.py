import collections
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nr = len(matrix)
        nc = len(matrix[0])

        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for i in range(nr):
            for j in range(nc):
                for sub_i, sub_j in (
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1),
                ):
                    if (
                        0 <= sub_i < nr
                        and 0 <= sub_j < nc
                        and matrix[sub_i][sub_j] > matrix[i][j]
                    ):
                        graph[(i, j)].append((sub_i, sub_j))
                        indegree[(sub_i, sub_j)] += 1

        queue = collections.deque()
        for i in range(nr):
            for j in range(nc):
                if indegree[(i, j)] == 0:
                    queue.append((i, j))

        result = 0
        while queue:
            n_queue = len(queue)
            for _ in range(n_queue):
                i, j = queue.popleft()
                for next_i, next_j in graph[(i, j)]:
                    indegree[(next_i, next_j)] -= 1
                    if indegree[(next_i, next_j)] == 0:
                        queue.append((next_i, next_j))
            result += 1
        return result

    def longestIncreasingPath_dp(self, matrix: List[List[int]]) -> int:
        def solve(matrix, dp, nr, nc, i, j):
            if dp[i][j] > 0:
                return dp[i][j]

            dp[i][j] = 1 + max(
                solve(matrix, dp, nr, nc, sub_i, sub_j)
                if (
                    0 <= sub_i < nr
                    and 0 <= sub_j < nc
                    and matrix[sub_i][sub_j] < matrix[i][j]
                )
                else 0
                for sub_i, sub_j in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
            )
            return dp[i][j]

        nr = len(matrix)
        nc = len(matrix[0])

        dp = [[0] * nc for _ in range(nr)]
        for i in range(nr):
            for j in range(nc):
                solve(matrix, dp, nr, nc, i, j)
        result = 0
        for i in range(nr):
            result = max(result, max(dp[i]))
        return result

    def longestIncreasingPath_dp_2(self, matrix: List[List[int]]) -> int:
        def solve(matrix, dp, nr, nc, i, j):
            if dp[i][j] > 0:
                return dp[i][j]

            for sub_i, sub_j in (
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1),
            ):
                if (
                    0 <= sub_i < nr
                    and 0 <= sub_j < nc
                    and matrix[sub_i][sub_j] > matrix[i][j]
                ):
                    dp[i][j] = max(
                        dp[i][j],
                        solve(matrix, dp, nr, nc, sub_i, sub_j),
                    )
            dp[i][j] += 1
            return dp[i][j]

        nr = len(matrix)
        nc = len(matrix[0])

        dp = [[0] * nc for _ in range(nr)]
        result = 0
        for i in range(nr):
            for j in range(nc):
                result = max(result, solve(matrix, dp, nr, nc, i, j))

        return result
