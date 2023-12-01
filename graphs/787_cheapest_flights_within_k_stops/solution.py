import collections
import heapq
import sys
from typing import List


class Solution:
    def find_cheapest_price_dfs(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = collections.defaultdict(list)
        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))
        self.total_price = sys.maxsize + 1
        self.find_cost_dfs(graph, src, dst, k + 1, 0)
        return -1 if self.total_price == sys.maxsize + 1 else self.total_price

    def find_cost_dfs(self, graph, src, dst, k, curr_price):
        if k < 0:
            return
        if src == dst:
            self.total_price = curr_price
            return
        if src not in graph:
            return
        for from_city, price in graph[src]:
            if curr_price + price > self.total_price:  # prune
                continue
            self.find_cost_dfs(graph, from_city, dst, k - 1, curr_price + price)

    def find_cheapest_price_bfs(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = collections.defaultdict(list)
        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))

        step = 0
        total_price = sys.maxsize + 1
        queue = collections.deque([(src, 0)])
        while queue:
            n_cities = len(queue)
            for _ in range(n_cities):
                from_city, curr_price = queue.popleft()
                if from_city == dst:
                    total_price = min(total_price, curr_price)
                if from_city not in graph:
                    continue
                for to_city, price in graph[from_city]:
                    if curr_price + price > total_price:  # prune
                        continue
                    queue.append((to_city, curr_price + price))
            if step > k:
                break
            step += 1

        return -1 if total_price == sys.maxsize + 1 else total_price

    def find_cheapest_price_bellman_ford(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        costs = [sys.maxsize + 1] * n

        costs[src] = 0
        for _ in range(k + 1):
            tmp = costs.copy()
            for from_city, to_city, price in flights:
                # Because we only process for k + 1 times, only process nodes
                # which can be reached from src in the current iteration
                if tmp[from_city] == sys.maxsize + 1:
                    continue
                tmp[to_city] = min(tmp[to_city], costs[from_city] + price)
            costs = tmp
        return -1 if costs[dst] == sys.maxsize + 1 else costs[dst]

    def find_cheapest_price_dijkstra(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = collections.defaultdict(list)
        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))
        h = [(0, src, k + 1)]
        heapq.heapify(h)
        while h:
            curr_price, from_city, step = heapq.heappop(h)
            if from_city == dst:
                return curr_price
            if step > 0:
                if from_city not in graph:
                    continue
                for to_city, price in graph[from_city]:
                    heapq.heappush(h, (curr_price + price, to_city, step - 1))
        return -1
