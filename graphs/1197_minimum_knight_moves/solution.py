import collections


class Solution:
    def minimumKnightMoves(self, x, y):
        # write your code here
        directions = [
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-1, -2),
            (-2, -1),
            (-2, 1),
            (-1, 2),
        ]
        seen = {(0, 0)}
        queue = collections.deque([(0, 0)])
        result = 0
        start = -100
        stop = 100
        while queue:
            n_nodes = len(queue)
            for _ in range(n_nodes):
                x0, y0 = queue.popleft()
                if x0 == x and y0 == y:
                    return result
                for dx, dy in directions:
                    xx = x0 + dx
                    yy = y0 + dy
                    if (
                        start <= xx <= stop
                        and start <= yy <= stop
                        and (xx, yy) not in seen
                    ):
                        seen.add((xx, yy))
                        queue.append((xx, yy))
            if queue:
                result += 1

    def minimumKnightMoves_prune(self, x, y):
        # write your code here
        directions = [
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-1, -2),
            (-2, -1),
            (-2, 1),
            (-1, 2),
        ]
        seen = {(0, 0)}
        queue = collections.deque([(0, 0)])
        result = 0
        while queue:
            n_nodes = len(queue)
            for _ in range(n_nodes):
                x0, y0 = queue.popleft()
                if x0 == x and y0 == y:
                    return result
                if x0 < -2 or y0 < -2 or x0 > x + 2 or y0 > y + 2:
                    continue
                for dx, dy in directions:
                    xx = x0 + dx
                    yy = y0 + dy
                    if (xx, yy) not in seen:
                        seen.add((xx, yy))
                        queue.append((xx, yy))
            if queue:
                result += 1
