import heapq
import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i, point in enumerate(points):
            heapq.heappush(h, (-(point[0] ** 2 + point[1] ** 2), i))
            if len(h) > k:
                heapq.heappop(h)
        result = [points[i] for _, i in h]
        return result

    def kClosest_quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        def quick_select(points, dists, k, l, r):
            pivot_index = random.randint(l, r)
            new_pivot_index = partition(dists, l, r, pivot_index)

            if new_pivot_index < k:
                return quick_select(points, dists, k, new_pivot_index + 1, r)
            if new_pivot_index > k:
                return quick_select(points, dists, k, l, new_pivot_index - 1)
            return [points[dists[i][1]] for i in range(k)]

        def partition(dists, l, r, pivot_index):
            pivot = dists[pivot_index]
            dists[r], dists[pivot_index] = dists[pivot_index], dists[r]

            idx = l
            for i in range(l, r):
                if dists[i][0] < pivot[0]:
                    dists[i], dists[idx] = dists[idx], dists[i]
                    idx += 1
            dists[r], dists[idx] = dists[idx], dists[r]
            return idx

        if k == len(points):
            return points
        dists = [(point[0] ** 2 + point[1] ** 2, i) for i, point in enumerate(points)]
        return quick_select(points, dists, k, 0, len(dists) - 1)
