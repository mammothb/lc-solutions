from typing import List


class Solution:
    """
    @param workers: Location of workers
    @param bikes: Location of bikes
    @return: Minimum sum of Manhattan distances
    """

    def assign_bikes_i_i(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        # write your code here
        nw = len(workers)
        nb = len(bikes)

        dp = [[float("inf")] * (1 << nb) for _ in range(nw + 1)]
        dp[0][0] = 0
        for w in range(nw):
            for b in range(1 << nb):
                for i in range(nb):
                    if (b >> i & 1) == 1:
                        dp[w + 1][b] = min(
                            dp[w + 1][b],
                            dp[w][b ^ (1 << i)] + self.dist(workers[w], bikes[i]),
                        )
        return min(dp[-1])

    def dist(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
