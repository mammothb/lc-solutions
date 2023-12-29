from typing import List

"""
# Definition for a QuadTree node.
"""


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        if not grid:
            return None

        if self.is_leaf(grid):
            return Node(grid[0][0], True, None, None, None, None)
        n = len(grid)
        return Node(
            grid[0][0],
            False,
            self.construct([grid[i][: n // 2] for i in range(n // 2)]),
            self.construct([grid[i][n // 2 :] for i in range(n // 2)]),
            self.construct([grid[i][: n // 2] for i in range(n // 2, n)]),
            self.construct([grid[i][n // 2 :] for i in range(n // 2, n)]),
        )

    def is_leaf(self, grid):
        return all(val == grid[0][0] for row in grid for val in row)

    def construct_2(self, grid: List[List[int]]) -> "Node":
        def solve(grid, i_start, j_start, i_stop, j_stop):
            if i_start == i_stop and j_start == j_stop:
                return Node(grid[i_start][j_start], True, None, None, None, None)

            i_mid = i_start + (i_stop - i_start) // 2
            j_mid = j_start + (j_stop - j_start) // 2

            top_left = solve(grid, i_start, j_start, i_mid, j_mid)
            top_right = solve(grid, i_start, j_mid + 1, i_mid, j_stop)
            bot_left = solve(grid, i_mid + 1, j_start, i_stop, j_mid)
            bot_right = solve(grid, i_mid + 1, j_mid + 1, i_stop, j_stop)

            if all(
                node.isLeaf for node in (top_left, top_right, bot_left, bot_right)
            ) and all(
                node.val == top_left.val
                for node in (top_left, top_right, bot_left, bot_right)
            ):
                return top_left
            return Node(
                top_left.val,
                False,
                top_left,
                top_right,
                bot_left,
                bot_right,
            )

        n = len(grid)
        return solve(grid, 0, 0, n - 1, n - 1)
