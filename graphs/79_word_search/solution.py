from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(board, visited, m, n, word, word_set, i, j, idx):
            if idx == len(word):
                return True
            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ii < m and 0 <= jj < n and not visited[ii][jj]:
                    if board[ii][jj] == word[idx]:
                        visited[ii][jj] = True
                        if solve(board, visited, m, n, word, word_set, ii, jj, idx + 1):
                            return True
                        visited[ii][jj] = False
                    elif board[ii][jj] not in word_set:
                        visited[ii][jj] = True
            return False

        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        word_set = set(word)
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if solve(board, visited, m, n, word, word_set, i, j, 1):
                        return True
                    visited[i][j] = False
                elif board[i][j] not in word_set:
                    visited[i][j] = True
        return False

    def exist_constant_space(self, board: List[List[str]], word: str) -> bool:
        def solve(board, m, n, word, i, j, idx):
            if idx == len(word):
                return True
            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == word[idx]:
                    old = board[ii][jj]
                    board[ii][jj] = "#"
                    if solve(board, m, n, word, ii, jj, idx + 1):
                        return True
                    board[ii][jj] = old
            return False

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    continue
                if board[i][j] == word[0]:
                    old = board[i][j]
                    board[i][j] = "#"
                    if solve(board, m, n, word, i, j, 1):
                        return True
                    board[i][j] = old
        return False
