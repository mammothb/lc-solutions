from typing import List

import pytest


class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        n = len(height)
        result = 0
        while i < n - 1:
            # Find the left height
            if height[i] <= height[i + 1]:
                i += 1
            else:
                l_height = height[i]
                j = i + 1
                r_height = 0
                r_idx = j
                # Find the right height thats:
                # 1. Taller than left height, or
                # 2. The rightmost tallest from [left+1, end]
                while j < n and r_height < l_height:
                    # Start counting right height only after we passed a valley
                    if height[j] <= height[j - 1]:
                        j += 1
                        continue
                    # Ignore some plateaus
                    if height[j] >= r_height and height[j] != height[j - 1]:
                        r_idx = j
                        r_height = height[j]
                    j += 1
                # Can only accumulate water up to the lower height
                h = min(l_height, r_height)
                for idx in range(i + 1, r_idx):
                    result += max(h - height[idx], 0)
                i = r_idx

        return result

    def trap_lr_array(self, height: List[int]) -> int:
        n = len(height)
        # tallest height from left
        l_heights = [height[0]]
        # tallest height from right
        r_heights = [height[-1]]
        for i in range(1, n):
            l_heights.append(max(l_heights[-1], height[i]))
            r_heights.append(max(r_heights[-1], height[n - 1 - i]))
        result = 0
        for i, h in enumerate(height):
            # area of each column, is the
            # (lower of either heights) - (curr column height)
            # ignore negative results
            result += max(0, min(l_heights[i], r_heights[n - 1 - i]) - h)
        return result

    def trap_two_pointer(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        max_l = 0
        max_r = 0
        result = 0
        while l <= r:
            # Process the lower side first
            if height[l] <= height[r]:
                if height[l] >= max_l:
                    max_l = height[l]
                else:
                    result += max_l - height[l]
                l += 1
            else:
                if height[r] >= max_r:
                    max_r = height[r]
                else:
                    result += max_r - height[r]
                r -= 1
        return result

    def trap_stack(self, height: List[int]) -> int:
        stack = []
        result = 0
        i = 0
        while i < len(height):
            # Append to stack until we pass a valley
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                curr = stack.pop()
                # only process if there's a valley, not just an uphill
                if stack:
                    result += (min(height[i], height[stack[-1]]) - height[curr]) * (
                        i - stack[-1] - 1
                    )
        return result


@pytest.mark.parametrize(
    "case,expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ],
)
def test_solution(case, expected):
    solution = Solution()
    assert solution.trap(case) == expected
    assert solution.trap_lr_array(case) == expected
    assert solution.trap_two_pointer(case) == expected
    assert solution.trap_stack(case) == expected
