import collections
import heapq
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        """Dijkstra"""
        probs = [0.0] * n
        probs[start_node] = 1.0

        graph = collections.defaultdict(list)
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        queue = [(-probs[start_node], start_node)]
        while queue:
            prob, node = heapq.heappop(queue)

            if node == end_node:
                return -prob
            if -prob < probs[node]:
                continue

            for next_node, next_prob in graph[node]:
                if next_prob * -prob > probs[next_node]:
                    probs[next_node] = next_prob * -prob
                    heapq.heappush(queue, (-probs[next_node], next_node))
        return 0.0
