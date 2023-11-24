from typing import List

import pytest


class Solution:
    def max_area(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            max_area = max(max_area, w * h)
            # impossible to get a larger value if we move the taller side
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area

    def max_area_optimized(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            max_area = max(max_area, w * h)
            # impossible to get a larger value if we move the taller side
            # we can also safely move the pointer until we find a taller side
            # due multiplication and decreasing the width
            while height[l] <= h and l < r:
                l += 1
            while height[r] <= h and l < r:
                r -= 1
        return max_area


@pytest.mark.parametrize(
    "case,expected", [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)]
)
def test_solution(case, expected):
    solution = Solution()
    assert solution.max_area(case) == expected
    assert solution.max_area_optimized(case) == expected
