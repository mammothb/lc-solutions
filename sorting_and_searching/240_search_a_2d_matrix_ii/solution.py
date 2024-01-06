from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr = len(matrix)
        nc = len(matrix[0])
        for row in matrix:
            if row[-1] < target:
                continue
            if row[0] <= target <= row[-1]:
                if self.contains(row, nc, target):
                    return True
            if row[0] > target:
                break
        return False

    def contains(self, row, n, target):
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if row[mid] == target:
                return True

            if row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

    def searchMatrix_2(self, matrix: List[List[int]], target: int) -> bool:
        # Treats the matrix like a bst
        nr = len(matrix)
        nc = len(matrix[0])
        i = 0
        j = nc - 1

        while i < nr and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False

    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        # Divide and conquer
        nr = len(matrix)
        nc = len(matrix[0])

        return self.search(matrix, 0, nr - 1, 0, nc - 1, target)

    def search(self, matrix, i_start, i_stop, j_start, j_stop, target):
        if i_start > i_stop or j_start > j_stop:
            return False

        i_mid = i_start + (i_stop - i_start) // 2
        j_mid = j_start + (j_stop - j_start) // 2
        mid = matrix[i_mid][j_mid]

        if mid == target:
            return True
        if mid < target:
            return (
                self.search(matrix, i_start, i_mid, j_mid + 1, j_stop, target)
                or self.search(matrix, i_mid + 1, i_stop, j_start, j_mid, target)
                or self.search(matrix, i_mid + 1, i_stop, j_mid + 1, j_stop, target)
            )
        return (
            self.search(matrix, i_start, i_mid - 1, j_start, j_mid - 1, target)
            or self.search(matrix, i_start, i_mid - 1, j_mid, j_stop, target)
            or self.search(matrix, i_mid, i_stop, j_start, j_mid - 1, target)
        )
