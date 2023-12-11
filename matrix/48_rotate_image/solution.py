from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        while i < n // 2:
            for idx in range(n - 1 - 2 * i):
                tmp = matrix[i][i + idx]
                matrix[i][i + idx] = matrix[n - 1 - i - idx][i]
                matrix[n - 1 - i - idx][i] = matrix[n - 1 - i][n - 1 - i - idx]
                matrix[n - 1 - i][n - 1 - i - idx] = matrix[i + idx][n - 1 - i]
                matrix[i + idx][n - 1 - i] = tmp
            i += 1

    def rotate_reverse_and_mirror(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
