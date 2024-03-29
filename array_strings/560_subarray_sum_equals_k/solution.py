from typing import Dict, List

import pytest


class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        result = 0
        sums: Dict[int, int] = {}
        curr = 0
        for num in nums:
            curr += num
            # Sum of current subarray from beginning matches
            if curr == k:
                result += 1
            # One of the subarrays until current index matches
            if curr - k in sums:
                result += sums[curr - k]

            if curr not in sums:
                sums[curr] = 1
            else:
                sums[curr] += 1

        return result

    def subarraySum_brute_force(self, nums: List[int], k: int) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            if curr == k:
                result += 1
            for j in range(i + 1, n):
                curr += nums[j]
                if curr == k:
                    result += 1
        return result

    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        # Initialize the seen dict so that the first subarray that's exactly k
        # will be
        seen = {0: 1}
        curr = 0
        for num in nums:
            curr += num
            if curr - k in seen:
                result += seen[curr - k]
            if curr in seen:
                seen[curr] += 1
            else:
                seen[curr] = 1
        return result


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("case,expected", [(([1, 1, 1], 2), 2), (([1, 2, 3], 3), 2)])
def test_solution(solution, case, expected):
    nums, k = case
    assert solution.subarray_sum(nums, k) == expected
