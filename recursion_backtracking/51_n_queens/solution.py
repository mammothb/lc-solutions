from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(board, n, i, j):
            for sub_j in range(n):
                if board[i][sub_j] == "Q":
                    return False

            # Only check diagonal from columns to the left
            # Check TLBR
            sub_i = i - 1
            sub_j = j - 1
            while 0 <= sub_i and 0 <= sub_j:
                if board[sub_i][sub_j] == "Q":
                    return False
                sub_i -= 1
                sub_j -= 1

            # Check TRBL
            sub_i = i + 1
            sub_j = j - 1
            while sub_i < n and 0 <= sub_j:
                if board[sub_i][sub_j] == "Q":
                    return False
                sub_i += 1
                sub_j -= 1
            return True

        def solve(board, n, j, result):
            if j == n:
                result.append(["".join(row) for row in board])
                return

            for i in range(n):
                if is_valid(board, n, i, j):
                    board[i][j] = "Q"
                    solve(board, n, j + 1, result)
                    board[i][j] = "."

        result = []
        board = [["."] * n for _ in range(n)]

        solve(board, n, 0, result)
        return result


print(Solution().solveNQueens(4))
