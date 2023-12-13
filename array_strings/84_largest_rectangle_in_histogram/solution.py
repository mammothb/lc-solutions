from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        result = 0
        for i in range(n):
            # Create monotonic increasing stack
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    idx = stack.pop()
                    if stack:
                        # Use stack[-1] because in 3,6,5,7, 1, 6 would have been
                        # already processed and removed from the stack when it's
                        # time to process 5. And sticking to the idea of finding
                        # the left and right indices of the first block that's
                        # smaller than the current block
                        area = (i - 1 - stack[-1]) * heights[idx]
                    else:
                        area = i * heights[idx]
                    result = max(result, area)
                stack.append(i)
        while stack:
            idx = stack.pop()
            if stack:
                area = (n - 1 - stack[-1]) * heights[idx]
            else:
                area = n * heights[idx]
            result = max(result, area)
        return result
