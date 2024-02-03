import collections
from typing import List


class Solution:
    """Description

    You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to
        represent INF as you may assume that the distance to a gate is less than
        2147483647.
    Fill each empty room with the distance to its nearest gate. If it is
    impossible to reach a Gate, that room should remain filled with INFS

    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        nr = len(rooms)
        nc = len(rooms[0])

        queue = collections.deque()
        for i in range(nr):
            for j in range(nc):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        inf = 2**31 - 1
        dist = 0
        while queue:
            dist += 1
            n_queue = len(queue)
            for _ in range(n_queue):
                i, j = queue.popleft()
                for next_i, next_j in (
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1),
                ):
                    if not (0 <= next_i < nr and 0 <= next_j < nc):
                        continue
                    if rooms[next_i][next_j] == inf:
                        rooms[next_i][next_j] = dist
                        queue.append((next_i, next_j))
