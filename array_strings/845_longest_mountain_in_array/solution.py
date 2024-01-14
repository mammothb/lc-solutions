from typing import List

import pytest


class Solution:
    def longest_mountain(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        # By start at 1, we're couning 1 less
        # 12321
        #  uudd
        i = 1
        while i < n:
            # Skip forward past plateau, so the climb up/down loop can iterate
            while i < n and arr[i - 1] == arr[i]:
                i += 1
            up = 0
            down = 0
            while i < n and arr[i - 1] < arr[i]:
                up += 1
                i += 1
            while i < n and arr[i - 1] > arr[i]:
                down += 1
                i += 1
            if up > 0 and down > 0:
                result = max(result, up + down + 1)
        return result if result >= 3 else 0

    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        max_length = 0

        left = 0
        while left < n - 2:
            while left < n - 1 and arr[left] >= arr[left + 1]:
                left += 1
            right = left + 1
            while right < n - 1 and arr[right] < arr[right + 1]:
                right += 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1
                max_length = max(max_length, right - left + 1)
            left = right
        return max_length


@pytest.mark.parametrize(
    "case,expected",
    [
        ([2, 1, 4, 7, 3, 2, 5], 5),
        ([2, 2, 2], 0),
    ],
)
def test_solution(case, expected):
    solution = Solution()
    assert solution.longest_mountain(case) == expected
