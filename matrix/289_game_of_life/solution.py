from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dies(board, nr, nc, i, j, neighbors):
            num_neighbors = 0
            for di, dj in neighbors:
                sub_i = i + di
                sub_j = j + dj
                if not (0 <= sub_i < nr and 0 <= sub_j < nc):
                    continue
                num_neighbors += board[sub_i][sub_j]
            return num_neighbors not in (2, 3)

        def revives(neighbor, nr, nc, i, j, neighbors):
            num_neighbors = 0
            for di, dj in neighbors:
                sub_i = i + di
                sub_j = j + dj
                if not (0 <= sub_i < nr and 0 <= sub_j < nc):
                    continue
                num_neighbors += board[sub_i][sub_j]
            return num_neighbors == 3

        neighbors = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]
        to_die = []
        to_revive = []
        nr = len(board)
        nc = len(board[0])
        for i in range(nr):
            for j in range(nc):
                if board[i][j] == 1:
                    if dies(board, nr, nc, i, j, neighbors):
                        to_die.append((i, j))
                else:
                    if revives(board, nr, nc, i, j, neighbors):
                        to_revive.append((i, j))
        for i, j in to_die:
            board[i][j] = 0
        for i, j in to_revive:
            board[i][j] = 1

    def gameOfLife_bit(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dies(board, nr, nc, i, j, neighbors):
            num_neighbors = 0
            for di, dj in neighbors:
                sub_i = i + di
                sub_j = j + dj
                if not (0 <= sub_i < nr and 0 <= sub_j < nc):
                    continue
                num_neighbors += board[sub_i][sub_j]
            return num_neighbors not in (2, 3)

        def revives(neighbor, nr, nc, i, j, neighbors):
            num_neighbors = 0
            for di, dj in neighbors:
                sub_i = i + di
                sub_j = j + dj
                if not (0 <= sub_i < nr and 0 <= sub_j < nc):
                    continue
                num_neighbors += board[sub_i][sub_j]
            return num_neighbors == 3

        neighbors = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]
        to_die = []
        to_revive = []
        nr = len(board)
        nc = len(board[0])
        for i in range(nr):
            for j in range(nc):
                if board[i][j] == 1:
                    if dies(board, nr, nc, i, j, neighbors):
                        to_die.append((i, j))
                else:
                    if revives(board, nr, nc, i, j, neighbors):
                        to_revive.append((i, j))
        for i, j in to_die:
            board[i][j] = 0
        for i, j in to_revive:
            board[i][j] = 1
