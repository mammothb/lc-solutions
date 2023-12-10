import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nr = len(matrix)
        nc = len(matrix[0])
        h = []
        for i in range(nr):
            for j in range(nc):
                if len(k) == k:
                    heapq.heappushpop(h, -matrix[i][j])
                else:
                    heapq.heappush(h, -matrix[i][j])
        return -h[0]

    def kthSmallest_minheap(self, matrix: List[List[int]], k: int) -> int:
        nr = len(matrix)
        nc = len(matrix[0])
        h = []
        for i in range(min(nr, k)):
            h.append((matrix[i][0], i, 0))
        heapq.heapify(h)

        result = -1
        for i in range(k):
            result, row, col = heapq.heappop(h)
            # Min heap, keeping exploring out of the smallest element
            if col < nc - 1:
                heapq.heappush(h, (matrix[row][col + 1], row, col + 1))
        return result

    def kthSmallest_binary_search(self, matrix: List[List[int]], k: int) -> int:
        nr = len(matrix)
        nc = len(matrix[0])
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2

            count = 0
            for i in range(nr):
                # Early exit since rows are ascending
                if matrix[i][0] > mid:
                    break
                # Count from back since rows are ascending
                for j in range(nc - 1, -1, -1):
                    if matrix[i][j] <= mid:
                        count += j + 1
                        break
            if count < k:
                lo = mid + 1
            else:
                # keep decreasing until count < k because mid might not exist
                # in the matrix
                result = mid
                hi = mid - 1
        return result
