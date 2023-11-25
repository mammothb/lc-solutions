from typing import List

import pytest


class Solution:
    def min_subarray_len(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        curr_sum = 0
        result = n
        # Keep extending the window to the right
        for i, num in enumerate(nums):
            curr_sum += num
            # Reduce left side of window while the sum still satifies target
            while curr_sum - nums[l] >= target:
                curr_sum -= nums[l]
                l += 1
            # Compute array length if we satify target
            if curr_sum >= target:
                result = min(result, i - l + 1)
        return result if curr_sum >= target else 0

    def min_subarray_len_binary_search(self, target: int, nums: List[int]) -> int:
        def find_left(sums, l, r, target):
            while l < r:
                mid = (l + r) // 2
                if sums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
                pass
            return l

        n = len(nums)
        result = n + 1
        l = 0
        # Compute cumulative sum
        for i in range(1, n):
            nums[i] += nums[i - 1]

        for r, s in enumerate(nums):
            if s >= target:
                l = find_left(nums, l, r, s - target)
                result = min(result, r - l + 1)
        return result if result <= n else 0


@pytest.mark.parametrize(
    "case,expected",
    [
        ((7, [2, 3, 1, 2, 4, 3]), 2),
        ((4, [1, 4, 4]), 1),
        ((11, [1, 1, 1, 1, 1, 1, 1, 1]), 0),
    ],
)
def test_solution(case, expected):
    target, nums = case
    solution = Solution()

    assert solution.min_subarray_len(target, nums) == expected
    assert solution.min_subarray_len_binary_search(target, nums) == expected
