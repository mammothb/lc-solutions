class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_valid(board, n, i, j):
            for sub_j in range(j):
                if board[i][sub_j]:
                    return False
            sub_i = i - 1
            sub_j = j - 1
            while 0 <= sub_i and 0 <= sub_j:
                if board[sub_i][sub_j]:
                    return False
                sub_i -= 1
                sub_j -= 1
            sub_i = i + 1
            sub_j = j - 1
            while sub_i < n and 0 <= sub_j:
                if board[sub_i][sub_j]:
                    return False
                sub_i += 1
                sub_j -= 1
            return True

        def solve(board, n, j, res):
            if j == n:
                res[0] += 1
                return
            for i in range(n):
                if is_valid(board, n, i, j):
                    board[i][j] = True
                    solve(board, n, j + 1, res)
                    board[i][j] = False

        board = [[False] * n for _ in range(n)]
        res = [0]
        solve(board, n, 0, res)
        return res[0]
