from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        nr = len(matrix)
        nc = len(matrix[0])
        self.prefix = [[0] * (nc + 1) for _ in range(nr + 1)]
        for i in range(1, nr + 1):
            for j in range(1, nc + 1):
                self.prefix[i][j] += (
                    self.prefix[i][j - 1]
                    + self.prefix[i - 1][j]
                    - self.prefix[i - 1][j - 1]
                    + matrix[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
