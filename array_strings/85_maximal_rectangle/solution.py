from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        nr = len(matrix)
        nc = len(matrix[0])
        heights = [0] * nc
        result = 0
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            stack = []
            for j in range(nc):
                while stack and heights[stack[-1]] > heights[j]:
                    center_height = heights[stack.pop()]
                    if stack:
                        area = center_height * (j - stack[-1] - 1)
                    else:
                        area = center_height * j
                    result = max(result, area)
                stack.append(j)
            while stack:
                center_height = heights[stack.pop()]
                if stack:
                    area = center_height * (nc - stack[-1] - 1)
                else:
                    area = center_height * nc
                result = max(result, area)

        return result
