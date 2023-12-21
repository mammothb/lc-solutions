import collections
from typing import List


class Solution:
    """
    @param grid: A m×n character matrix.
    @return: The length of the shortest path to obtain any cup of bubble tea.
    """

    def get_bubble_tea(self, grid: List[List[str]]) -> int:
        # --- write your code here ---
        queue = collections.deque()
        nr = len(grid)
        nc = len(grid[0])
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "*":
                    queue.append((i, j))
                    break
            if queue:
                break
        step = 0
        while queue:
            step += 1
            n_queue = len(queue)
            for _ in range(n_queue):
                i, j = queue.popleft()
                grid[i][j] = "X"
                for sub_i, sub_j in (
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1),
                ):
                    if (
                        0 <= sub_i < nr
                        and 0 <= sub_j < nc
                        and grid[sub_i][sub_j] != "X"
                    ):
                        if grid[sub_i][sub_j] == "#":
                            return step
                        queue.append((sub_i, sub_j))
        return -1
