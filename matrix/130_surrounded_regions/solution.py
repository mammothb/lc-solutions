from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def save(board, nr, nc, i, j):
            if board[i][j] == "#":
                return
            board[i][j] = "#"

            for sub_i, sub_j in (
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1),
            ):
                if 0 <= sub_i < nr and 0 <= sub_j < nc and board[sub_i][sub_j] == "O":
                    save(board, nr, nc, sub_i, sub_j)

        nr = len(board)
        nc = len(board[0])
        for i in range(nr):
            if board[i][0] == "O":
                save(board, nr, nc, i, 0)
            if board[i][nc - 1] == "O":
                save(board, nr, nc, i, nc - 1)
        for j in range(nc):
            if board[0][j] == "O":
                save(board, nr, nc, 0, j)
            if board[nr - 1][j] == "O":
                save(board, nr, nc, nr - 1, j)
        for i in range(nr):
            for j in range(nc):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
