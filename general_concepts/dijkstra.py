import collections
import heapq
import sys


def dijkstra(num_vertices, edges, src, dst):
    costs = [sys.maxsize + 1] * num_vertices
    costs[src] = 0
    seen = [False] * num_vertices
    seen[src] = True
    prev = list(range(num_vertices))
    # Create adjacency list
    graph = collections.defaultdict(list)
    for from_vertex, to_vertex, cost in edges:
        graph[from_vertex].append((to_vertex, cost))
        graph[to_vertex].append((from_vertex, cost))
    h = []
    for neighbor_vertex, cost in graph[src]:
        heapq.heappush(h, (cost, neighbor_vertex, src))
    while h:
        curr_cost, vertex, parent_vertex = heapq.heappop(h)
        if seen[vertex]:
            continue
        costs[vertex] = curr_cost
        seen[vertex] = True
        prev[vertex] = parent_vertex
        for neighbor_vertex, cost in graph[vertex]:
            if not seen[neighbor_vertex]:
                heapq.heappush(h, (curr_cost + cost, neighbor_vertex, vertex))
    if costs[dst] == sys.maxsize + 1:
        return -1, []
    path = [prev[dst]]
    while path[-1] != src:
        path.append(prev[path[-1]])
    return costs[dst], list(reversed(path))


#            3 --(2)---+
#            ^         |
#           (3)        |
#            |         v
#  0 --(4)-> 2 --(6)-> 5
#  |         ^ \       ^
# (4)        | (1)    (3)
#  v         |  _\|    |
#  1 --(2)---+    4 ---+
graph = [
    (0, 1, 4),
    (0, 2, 4),
    (1, 2, 2),
    (2, 3, 3),
    (2, 4, 1),
    (2, 5, 6),
    (3, 5, 2),
    (4, 5, 3),
]
print(dijkstra(6, graph, 0, 5))
