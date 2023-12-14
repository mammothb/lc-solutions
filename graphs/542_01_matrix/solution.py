import collections
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        nr = len(mat)
        nc = len(mat[0])

        queue = collections.deque()
        for i in range(nr):
            for j in range(nc):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    # Mark not visited
                    mat[i][j] = -1
        while queue:
            i, j = queue.popleft()
            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                # Only move to unprocess cells
                if 0 <= ii < nr and 0 <= jj < nc and mat[ii][jj] == -1:
                    mat[ii][jj] = mat[i][j] + 1
                    queue.append((ii, jj))
        return mat
