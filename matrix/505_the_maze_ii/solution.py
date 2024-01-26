import heapq
from typing import List


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """

    def shortest_distance(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> int:
        # write your code here
        nr = len(maze)
        nc = len(maze[0])

        dists = [[float("inf")] * nc for _ in range(nr)]
        dists[start[0]][start[1]] = 0

        queue = [(0, start[0], start[1])]
        while queue:
            dist, i, j = heapq.heappop(queue)

            if [i, j] == destination:
                return dist
            if dist > dists[i][j]:
                continue
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_i = i
                next_j = j
                step = 0
                while (
                    0 <= next_i + di < nr
                    and 0 <= next_j + dj < nc
                    and maze[next_i + di][next_j + dj] == 0
                ):
                    next_i += di
                    next_j += dj
                    step += 1
                if dist + step < dists[next_i][next_j]:
                    dists[next_i][next_j] = dist + step
                    heapq.heappush(
                        queue,
                        (dists[next_i][next_j], next_i, next_j),
                    )
        return -1
