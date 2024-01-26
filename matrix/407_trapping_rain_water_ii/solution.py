import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        nr = len(heightMap)
        nc = len(heightMap[0])

        queue = []
        for i in range(nr):
            queue.append((heightMap[i][0], i, 0))
            queue.append((heightMap[i][nc - 1], i, nc - 1))
            heightMap[i][0] = -1
            heightMap[i][nc - 1] = -1
        for j in range(1, nc - 1):
            queue.append((heightMap[0][j], 0, j))
            queue.append((heightMap[nr - 1][j], nr - 1, j))
            heightMap[0][j] = -1
            heightMap[nr - 1][j] = -1
        heapq.heapify(queue)

        result = 0
        level = 0
        while queue:
            height, i, j = heapq.heappop(queue)
            level = max(level, height)
            for next_i, next_j in (
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1),
            ):
                if not (0 <= next_i < nr and 0 <= next_j < nc):
                    continue
                if heightMap[next_i][next_j] == -1:
                    continue
                if heightMap[next_i][next_j] < level:
                    result += level - heightMap[next_i][next_j]
                heapq.heappush(queue, (heightMap[next_i][next_j], next_i, next_j))
                heightMap[next_i][next_j] = -1
        return result
