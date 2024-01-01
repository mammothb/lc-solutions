import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        # Sort capital and profits in ascending order according to captital
        capital, profits = zip(*sorted(zip(capital, profits), key=lambda x: x[0]))

        if w < capital[0]:
            return 0

        h = []
        num_project = 0
        i = 0
        n = len(profits)
        while num_project < k:
            while i < n and capital[i] <= w:
                heapq.heappush(h, -profits[i])
                i += 1
            # Early stop if we ran out of projects to start
            if not h:
                break
            w += -heapq.heappop(h)
            num_project += 1

        return w

    def findMaximizedCapital_two_heap(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        # To store capital in ascending order
        min_heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_heap)

        # To store profits of available projects
        max_heap = []
        for _ in range(k):
            while min_heap and min_heap[0][0] <= w:
                heapq.heappush(max_heap, -heapq.heappop(min_heap)[1])
            # Early stop
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
        return w
