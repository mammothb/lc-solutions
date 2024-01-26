import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, time in times:
            graph[a - 1].append((b - 1, time))

        k -= 1
        times = [float("inf")] * n
        times[k] = 0
        queue = [(0, k)]
        while queue:
            time, node = heapq.heappop(queue)
            if time > times[node]:
                continue
            for next_node, next_time in graph[node]:
                if time + next_time < times[next_node]:
                    times[next_node] = time + next_time
                    heapq.heappush(queue, (times[next_node], next_node))
        result = max(times)
        if result == float("inf"):
            return -1
        return result
