import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def to_index(cell, n):
            row, col = divmod(cell - 1, n)
            if row % 2 == 0:
                return n - 1 - row, col
            return n - 1 - row, n - 1 - col

        n = len(board)
        target = n**2
        visited = set()
        queue = collections.deque([(1, 0)])
        while queue:
            cell, step = queue.popleft()
            i, j = to_index(cell, n)
            if board[i][j] != -1:
                cell = board[i][j]
            if cell == target:
                return step
            for next_cell in range(cell + 1, min(cell + 6, target) + 1):
                if next_cell not in visited:
                    visited.add(next_cell)
                    queue.append((next_cell, step + 1))
        return -1
