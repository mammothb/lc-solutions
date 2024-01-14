from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        nr = len(matrix)
        nc = len(matrix[0])
        heights = [0] * nc
        result = 0
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            sorted_heights = sorted(heights, reverse=True)
            for j in range(nc):
                result = max(result, sorted_heights[j] * (j + 1))
        return result
