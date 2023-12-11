from typing import List

DIM = 9
SUB_DIM = 3


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def box_idx(i, j):
            return (i // SUB_DIM) * SUB_DIM + (j // SUB_DIM)

        row = [0] * DIM
        col = [0] * DIM
        box = [0] * DIM

        for i in range(DIM):
            for j in range(DIM):
                if board[i][j] == ".":
                    continue
                val = int(board[i][j])
                if (
                    (row[i] >> val & 1)
                    or (col[j] >> val & 1)
                    or (box[box_idx(i, j)] >> val & 1)
                ):
                    return False
                row[i] |= 1 << val
                col[j] |= 1 << val
                box[box_idx(i, j)] |= 1 << val
        return True
