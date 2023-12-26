import collections
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        graph = collections.defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)

        seen = set()
        queue = collections.deque([source])
        result = 0
        while queue:
            result += 1
            n_queue = len(queue)
            for _ in range(n_queue):
                src = queue.popleft()
                for bus in graph:
                    if bus in seen:
                        continue
                    seen.add(bus)
                    for dst in routes[bus]:
                        if dst == target:
                            return result
                        if src == dst:
                            continue
                        queue.append(dst)
        return -1
