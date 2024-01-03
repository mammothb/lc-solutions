import collections
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        nr = len(maze)
        nc = len(maze[0])

        queue = collections.deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        step = 0
        while queue:
            i, j, step = queue.popleft()
            if step > 0 and (i in (0, nr - 1) or j in (0, nc - 1)):
                return step

            for sub_i, sub_j in (
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1),
            ):
                if 0 <= sub_i < nr and 0 <= sub_j < nc and maze[sub_i][sub_j] == ".":
                    maze[sub_i][sub_j] = "+"
                    queue.append((sub_i, sub_j, step + 1))

        return -1
