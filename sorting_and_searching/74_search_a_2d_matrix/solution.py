from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr = len(matrix)
        nc = len(matrix[0])

        i_lo = 0
        i_hi = nr - 1
        while i_lo <= i_hi:
            i_mid = (i_lo + i_hi) // 2
            if matrix[i_mid][0] == target:
                return True
            if matrix[i_mid][0] > target:
                i_hi = i_mid - 1
            else:
                i_lo = i_mid + 1
        i = i_hi
        j_lo = 0
        j_hi = nc - 1
        while j_lo <= j_hi:
            j_mid = (j_lo + j_hi) // 2
            if matrix[i][j_mid] == target:
                return True
            if matrix[i][j_mid] < target:
                j_lo = j_mid + 1
            else:
                j_hi = j_mid - 1
        return False
