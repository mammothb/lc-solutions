import collections
from typing import List


class Solution:
    def flood_fill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        target = image[sr][sc]
        if target == color:
            return image
        self.fill_dfs(image, sr, sc, color, target, len(image), len(image[0]))
        return image

    def flood_fill_bfs(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        target = image[sr][sc]
        if target != color:
            nr = len(image)
            nc = len(image[0])
            queue = collections.deque([(sr, sc)])
            while queue:
                i, j = queue.popleft()
                image[i][j] = color
                for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= ii < nr and 0 <= jj < nc and image[ii][jj] == target:
                        queue.append((ii, jj))
        return image

    def fill_dfs(self, image, i, j, color, target, nr, nc):
        if not (0 <= i < nr and 0 <= j < nc) or image[i][j] != target:
            return
        image[i][j] = color
        self.fill_dfs(image, i + 1, j, color, target, nr, nc)
        self.fill_dfs(image, i - 1, j, color, target, nr, nc)
        self.fill_dfs(image, i, j + 1, color, target, nr, nc)
        self.fill_dfs(image, i, j - 1, color, target, nr, nc)

    def floodFill_dfs(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        def dfs(image, nr, nc, i, j, color, src_color):
            for ii, jj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ii < nr and 0 <= jj < nc and image[ii][jj] == src_color:
                    image[ii][jj] = color
                    dfs(image, nr, nc, ii, jj, color, src_color)

        nr = len(image)
        nc = len(image[0])
        src_color = image[sr][sc]
        if src_color == color:
            return image

        image[sr][sc] = color
        dfs(image, nr, nc, sr, sc, color, src_color)

        return image
