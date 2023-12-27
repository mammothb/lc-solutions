from typing import List

DIM = 9
SUB_DIM = 3
NUMS = "123456789"


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(board, i, j, val):
            if any(board[ii][j] == val for ii in range(DIM)) or any(
                board[i][jj] == val for jj in range(DIM)
            ):
                return False

            i_start = int(i / SUB_DIM) * SUB_DIM
            j_start = int(j / SUB_DIM) * SUB_DIM
            for ii in range(SUB_DIM):
                for jj in range(SUB_DIM):
                    if board[ii + i_start][jj + j_start] == val:
                        return False

            return True

        def solve(board, i, j):
            if i == DIM - 1 and j == DIM:
                return True

            if j == DIM:
                i += 1
                j = 0
            if board[i][j] != ".":
                return solve(board, i, j + 1)

            for num in NUMS:
                if is_valid(board, i, j, num):
                    board[i][j] = num

                    if solve(board, i, j + 1):
                        return True

                    board[i][j] = "."
            return False

        solve(board, 0, 0)

    def solveSudoku_2(self, board: List[List[str]]) -> None:
        """Use bitmasks."""

        def box_idx(i, j):
            return int(i / SUB_DIM) * SUB_DIM + int(j / SUB_DIM)

        def is_valid(i, j, val):
            ival = int(val)
            return (
                not (self.row[i] >> ival & 1)
                and not (self.col[j] >> ival & 1)
                and not (self.box[box_idx(i, j)] >> ival & 1)
            )

        def solve(board, i, j):
            if i == DIM - 1 and j == DIM:
                return True

            if j == DIM:
                i += 1
                j = 0
            if board[i][j] != ".":
                return solve(board, i, j + 1)

            for num in NUMS:
                if is_valid(i, j, num):
                    board[i][j] = num
                    inum = int(num)
                    self.row[i] |= 1 << inum
                    self.col[j] |= 1 << inum
                    self.box[box_idx(i, j)] |= 1 << inum

                    if solve(board, i, j + 1):
                        return True

                    board[i][j] = "."
                    self.row[i] &= ~(1 << inum)
                    self.col[j] &= ~(1 << inum)
                    self.box[box_idx(i, j)] &= ~(1 << inum)
            return False

        self.row = [0] * DIM
        self.col = [0] * DIM
        self.box = [0] * DIM
        for i in range(DIM):
            for j in range(DIM):
                if board[i][j] == ".":
                    continue
                self.row[i] |= 1 << int(board[i][j])
                self.col[j] |= 1 << int(board[i][j])
                self.box[box_idx(i, j)] |= 1 << int(board[i][j])

        solve(board, 0, 0)

    def solveSudoku_3(self, board: List[List[str]]) -> None:
        """Bitmasks, alternative ways to test and toggle."""

        def box_idx(i, j):
            return (i // SUB_DIM) * SUB_DIM + j // SUB_DIM

        def is_valid(row, col, box, i, j, num):
            return (
                ((row[i] >> num) & 1)
                | ((col[j] >> num) & 1)
                | ((box[box_idx(i, j)] >> num) & 1)
            ) == 0

        def solve(board, row, col, box, i, j):
            if i == DIM - 1 and j == DIM:
                return True

            if j == DIM:
                i += 1
                j = 0

            if board[i][j] != ".":
                return solve(board, row, col, box, i, j + 1)

            for num in NUMS:
                inum = int(num)
                if is_valid(row, col, box, i, j, inum):
                    board[i][j] = num
                    row[i] |= 1 << inum
                    col[j] |= 1 << inum
                    box[box_idx(i, j)] |= 1 << inum
                    if solve(board, row, col, box, i, j + 1):
                        return True
                    board[i][j] = "."
                    row[i] ^= 1 << inum
                    col[j] ^= 1 << inum
                    box[box_idx(i, j)] ^= 1 << inum
            return False

        row = [0] * DIM
        col = [0] * DIM
        box = [0] * DIM
        for i in range(DIM):
            for j in range(DIM):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                row[i] |= 1 << num
                col[j] |= 1 << num
                box[box_idx(i, j)] |= 1 << num

        solve(board, row, col, box, 0, 0)
