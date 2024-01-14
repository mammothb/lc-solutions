from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        nr = len(mat)
        nc = len(mat[0])
        prefix = [[0] * (nc + 1) for _ in range(nr + 1)]
        for i in range(1, nr + 1):
            for j in range(1, nc + 1):
                prefix[i][j] += (
                    prefix[i][j - 1]
                    + prefix[i - 1][j]
                    - prefix[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )
        for i in range(nr):
            for j in range(nc):
                mat[i][j] = self.sum_region(
                    prefix,
                    max(0, i - k),
                    max(0, j - k),
                    min(nr - 1, i + k),
                    min(nc - 1, j + k),
                )
        return mat

    def sum_region(self, prefix, row1, col1, row2, col2):
        return (
            prefix[row2 + 1][col2 + 1]
            - prefix[row1][col2 + 1]
            - prefix[row2 + 1][col1]
            + prefix[row1][col1]
        )
