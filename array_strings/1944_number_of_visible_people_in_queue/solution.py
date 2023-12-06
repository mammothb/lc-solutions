from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0] * n
        stack = [n - 1]
        for i in range(n - 2, -1, -1):
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
                result[i] += 1
            if stack:
                result[i] += 1
            stack.append(i)
        return result


#  print(Solution().canSeePersonsCount([10, 6, 8, 5, 11, 9]))
print(Solution().canSeePersonsCount([12, 6, 8, 5, 11, 9, 14, 8]))
