from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        nr = len(matrix)
        nc = len(matrix[0])
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            for j in range(nc):
                matrix[row][j] = 0
        for col in cols:
            for i in range(nr):
                matrix[i][col] = 0

    def setZeroes_Omn_space(self, matrix: List[List[int]]) -> None:
        nr = len(matrix)
        nc = len(matrix[0])
        rows = [False] * nr
        cols = [False] * nc
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        for i in range(nr):
            for j in range(nc):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

    def setZeroes_constant_space(self, matrix: List[List[int]]) -> None:
        nr = len(matrix)
        nc = len(matrix[0])
        zero_first_row = False
        zero_first_col = False
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_first_row = True
                    if j == 0:
                        zero_first_col = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, nr):
            for j in range(1, nc):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if zero_first_row:
            for j in range(nc):
                matrix[0][j] = 0
        if zero_first_col:
            for i in range(nr):
                matrix[i][0] = 0
