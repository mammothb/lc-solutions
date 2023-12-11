from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nr = len(matrix)
        nc = len(matrix[0])
        result = []

        top = 0
        left = 0
        bottom = nr - 1
        right = nc - 1

        while top < bottom and left < right:
            for j in range(left, right):
                result.append(matrix[top][j])
            for i in range(top, bottom):
                result.append(matrix[i][right])
            for j in range(right, left, -1):
                result.append(matrix[bottom][j])
            for i in range(bottom, top, -1):
                result.append(matrix[i][left])
            top += 1
            left += 1
            bottom -= 1
            right -= 1

        if len(result) < nr * nc:
            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    result.append(matrix[i][j])

        return result
