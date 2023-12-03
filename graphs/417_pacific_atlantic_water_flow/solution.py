from typing import List


class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        nr = len(heights)
        nc = len(heights[0])

        tl_stack = []
        br_stack = []
        for i in range(nr):
            tl_stack.append((i, 0))
            br_stack.append((i, nc - 1))
        for j in range(nc):
            tl_stack.append((0, j))
            br_stack.append((nr - 1, j))

        tl_visited = self.flood(heights, tl_stack, nr, nc)
        br_visited = self.flood(heights, br_stack, nr, nc)

        # Overlapping nodes are nodes which can reach both oceans
        for i in range(nr):
            for j in range(nc):
                if tl_visited[i][j] and br_visited[i][j]:
                    result.append([i, j])

        return result

    def flood(self, heights, stack, nr, nc):
        visited = [[False] * nc for _ in range(nr)]

        # Flood the island using DFS
        while stack:
            i, j = stack.pop()
            visited[i][j] = True

            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (
                    0 <= ii < nr
                    and 0 <= jj < nc
                    and not visited[ii][jj]
                    and heights[ii][jj] >= heights[i][j]
                ):
                    stack.append((ii, jj))
        return visited

    def pacific_atlantic_recursive(self, heights: List[List[int]]) -> List[List[int]]:
        def flood(heights, visited, nr, nc, i, j):
            if visited[i][j]:
                return
            visited[i][j] = True
            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ii < nr and 0 <= jj < nc:
                    if not visited[ii][jj] and heights[ii][jj] >= heights[i][j]:
                        flood(heights, visited, nr, nc, ii, jj)

        result = []
        nr = len(heights)
        nc = len(heights[0])
        tl_visited = [[False] * nc for _ in range(nr)]
        br_visited = [[False] * nc for _ in range(nr)]

        for i in range(nr):
            flood(heights, tl_visited, nr, nc, i, 0)
            flood(heights, br_visited, nr, nc, i, nc - 1)
        for j in range(nc):
            flood(heights, tl_visited, nr, nc, 0, j)
            flood(heights, br_visited, nr, nc, nr - 1, j)

        for i in range(nr):
            for j in range(nc):
                if tl_visited[i][j] and br_visited[i][j]:
                    result.append([i, j])

        return result
