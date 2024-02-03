import collections
from typing import List


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """

    def has_path(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        # write your code here
        nr = len(maze)
        nc = len(maze[0])

        visited = set()
        visited.add((start[0], start[1]))
        queue = collections.deque([(start[0], start[1])])
        while queue:
            i, j = queue.popleft()

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_i = i
                next_j = j
                # Roll until obstacle or wall
                while (
                    0 <= next_i + di < nr
                    and 0 <= next_j + dj < nc
                    and maze[next_i + di][next_j + dj] == 0
                ):
                    next_i += di
                    next_j += dj
                if [next_i, next_j] == destination:
                    return True
                if (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    queue.append((next_i, next_j))
        return False

    def has_path_dfs(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        # write your code here
        nr = len(maze)
        nc = len(maze[0])
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        return self.dfs(
            maze,
            visited,
            nr,
            nc,
            start[0],
            start[1],
            destination[0],
            destination[1],
        )

    def dfs(self, maze, visited, nr, nc, i, j, i_dst, j_dst):
        if i == i_dst and j == j_dst:
            return True
        if (i, j) in visited:
            return False
        visited.add((i, j))
        for di, dj in self.dirs:
            ni = i
            nj = j
            while (
                0 <= ni + di < nr and 0 <= nj + dj < nc and maze[ni + di][nj + dj] != 1
            ):
                ni += di
                nj += dj
            if self.dfs(maze, visited, nr, nc, ni, nj, i_dst, j_dst):
                return True
        return False
