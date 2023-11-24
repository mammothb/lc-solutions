from collections import defaultdict, deque


class Graph:
    def __init__(self, num_vertices):
        self.graph = defaultdict(list)
        self.num_vertices = num_vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_acyclic_bfs(self):
        indegrees = [0] * self.num_vertices
        for neighbors in self.graph.values():
            for node in neighbors:
                indegrees[node] += 1
        queue = deque()
        for node, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(node)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in self.graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return count == self.num_vertices

    def is_acyclic_dfs(self):
        checked = [False] * self.num_vertices
        stack = [False] * self.num_vertices

        for node in range(self.num_vertices):
            if not checked[node] and not self._is_acyclic_dfs(checked, stack, node):
                return False
        return True

    def _is_acyclic_dfs(self, checked, stack, node):
        if checked[node]:
            return True
        if stack[node]:
            return False
        stack[node] = True
        for neighbor in self.graph[node]:
            if not self._is_acyclic_dfs(checked, stack, neighbor):
                return False
        stack[node] = False
        checked[node] = True
        return True


if __name__ == "__main__":
    # + 0 < 1
    # |  |\ ^
    # +---> 2 <- 3
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)

    print(f"{graph.is_acyclic_dfs()=}")
    print(f"{graph.is_acyclic_bfs()=}")

    # 0 < 1
    #  |\ ^
    #     2 <- 3
    graph_2 = Graph(4)
    graph_2.add_edge(0, 1)
    graph_2.add_edge(0, 2)
    graph_2.add_edge(1, 2)
    graph_2.add_edge(2, 3)

    print(f"{graph_2.is_acyclic_dfs()=}")
    print(f"{graph_2.is_acyclic_bfs()=}")

    # 0 < 1
    #  |\ ^    +---+
    #     2 <- 3 <-+
    graph_3 = Graph(4)
    graph_3.add_edge(0, 1)
    graph_3.add_edge(0, 2)
    graph_3.add_edge(1, 2)
    graph_3.add_edge(2, 3)
    graph_3.add_edge(3, 3)

    print(f"{graph_3.is_acyclic_dfs()=}")
    print(f"{graph_3.is_acyclic_bfs()=}")
