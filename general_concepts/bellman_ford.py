import sys
from typing import List, Tuple


def bellman_ford(
    num_vertices: int, edges: List[Tuple[int, int, int]], src: int
) -> bool:
    # Stores distance from `src`
    costs = [sys.maxsize + 1] * num_vertices
    costs[src] = 0

    # Relax for num_vertices - 1 times
    for _ in range(num_vertices - 1):
        # Need to create tmp cost array if we're interested in counting
        # distance from source at each step
        tmp = costs.copy()
        for from_vertex, to_vertex, cost in edges:
            if (
                tmp[from_vertex] != sys.maxsize + 1
                and tmp[from_vertex] + cost < costs[to_vertex]
            ):
                costs[to_vertex] = tmp[from_vertex] + cost

    # Detect negative cycle
    for from_vertex, to_vertex, cost in edges:
        if costs[from_vertex] + cost < costs[to_vertex]:
            return True
    return False


def bellman_ford_no_copy(
    num_vertices: int, edges: List[Tuple[int, int, int]], src: int
) -> bool:
    # Stores distance from `src`
    costs = [sys.maxsize + 1] * num_vertices
    costs[src] = 0

    # Relax for num_vertices - 1 times
    for _ in range(num_vertices - 1):
        # without a tmp array, the cost at ith relaxation step may not
        # represent the true distance from `src` in i steps, but the
        # property of shortest distance not decreasing in a graph with no
        # negative cycle holds
        for from_vertex, to_vertex, cost in edges:
            if costs[from_vertex] + cost < costs[to_vertex]:
                costs[to_vertex] = costs[from_vertex] + cost

    # Detect negative cycle
    for from_vertex, to_vertex, cost in edges:
        if costs[from_vertex] + cost < costs[to_vertex]:
            return True
    return False


def bellman_ford_shortest_path(
    num_vertices: int, edges: List[Tuple[int, int, int]], src: int, dst: int
) -> List[int]:
    # Stores distance from `src`
    costs = [sys.maxsize + 1] * num_vertices
    parents = [-1] * num_vertices
    costs[src] = 0
    parents[src] = src

    # Relax for num_vertices - 1 times
    for _ in range(num_vertices - 1):
        for from_vertex, to_vertex, cost in edges:
            if costs[from_vertex] + cost < costs[to_vertex]:
                costs[to_vertex] = costs[from_vertex] + cost
                parents[to_vertex] = from_vertex
    if parents[dst] == -1:
        return []
    result = [dst, parents[dst]]
    while result[-1] != src:
        result.append(parents[result[-1]])

    return list(reversed(result))


def bellman_ford_shortest_path_k_steps(
    num_vertices: int, edges: List[Tuple[int, int, int]], src: int, dst: int, k: int
) -> List[int]:
    # Stores distance from `src`
    costs = [sys.maxsize + 1] * num_vertices
    parents = [-1] * num_vertices
    costs[src] = 0
    parents[src] = src

    for _ in range(k):
        tmp = costs.copy()
        # Need to create tmp cost array if we're interested in counting
        # distance from source at each step
        for from_vertex, to_vertex, cost in edges:
            if (
                tmp[from_vertex] != sys.maxsize + 1
                and tmp[from_vertex] + cost < costs[to_vertex]
            ):
                costs[to_vertex] = tmp[from_vertex] + cost
                parents[to_vertex] = from_vertex
    if parents[dst] == -1:
        return []
    result = [dst, parents[dst]]
    while result[-1] != src:
        result.append(parents[result[-1]])

    return list(reversed(result))


if __name__ == "__main__":
    # 0 --( 5)-> 1 --( 2)-> 3 --( 2)-> 5
    #            |          ^          |
    #          ( 1)       (-1)       (-3)
    #            v          |          |
    #            2 --( 1)-> 4 <--------+
    graph_w_neg_cycle = [
        (0, 1, 5),
        (1, 2, 1),
        (1, 3, 2),
        (2, 4, 1),
        (3, 5, 2),
        (4, 3, -1),
        (5, 4, -3),
    ]
    # 0 --( 5)-> 1 --( 2)-> 3 --( 2)-> 5
    #            |          ^
    #          ( 1)       (-1)
    #            v          |
    #            2 --( 1)-> 4
    graph_wo_neg_cycle = [
        (0, 1, 5),
        (1, 2, 1),
        (1, 3, 2),
        (2, 4, 1),
        (3, 5, 2),
        (4, 3, -1),
    ]
    # 0 --( 5)-> 1 --( 2)-> 4 --( 2)-> 5
    #            |                     ^
    #          ( 1)                    |
    #            v                     |
    #            2 --( 1)-> 3 --( 2)---+
    graph_competing_paths = [
        (0, 1, 5),
        (1, 2, 1),
        (1, 4, 2),
        (2, 3, 1),
        (3, 5, 2),
        (4, 5, 2),
    ]
    print(bellman_ford(6, graph_w_neg_cycle, 0))
    print(bellman_ford_no_copy(6, graph_w_neg_cycle, 0))
    print(bellman_ford(6, graph_wo_neg_cycle, 0))
    print(bellman_ford_no_copy(6, graph_wo_neg_cycle, 0))

    print(bellman_ford_shortest_path(6, graph_wo_neg_cycle, 0, 5))
    # will pick whichever lowest cost path that comes first. Doesn't minimize
    # number of steps
    print(bellman_ford_shortest_path(6, graph_competing_paths, 0, 5))

    print(bellman_ford_shortest_path_k_steps(6, graph_wo_neg_cycle, 0, 5, 3))
    print(bellman_ford_shortest_path_k_steps(6, graph_competing_paths, 0, 5, 3))
