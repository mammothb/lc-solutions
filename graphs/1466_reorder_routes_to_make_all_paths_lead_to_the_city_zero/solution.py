import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = collections.defaultdict(list)
        for from_city, to_city in connections:
            graph[from_city].append(to_city)
            graph[to_city].append(from_city)
            roads.add((from_city, to_city))

        result = 0
        stack = [(0, -1)]
        while stack:
            city, from_city = stack.pop()
            if (from_city, city) in roads:
                result += 1
            for to_city in graph[city]:
                if to_city == from_city:
                    continue
                stack.append((to_city, city))
        return result
