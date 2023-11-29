from typing import List

import pytest


class Solution:
    def split_array(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(nums)
        if k >= len(nums):
            return max(nums)

        min_subarray_sum = max(nums)
        max_subarray_sum = sum(nums)

        while min_subarray_sum < max_subarray_sum:
            mid_subarray_sum = (min_subarray_sum + max_subarray_sum) // 2
            # ---
            curr = 0
            num_subarray = 1
            for num in nums:
                if curr + num > mid_subarray_sum:
                    curr = 0
                    num_subarray += 1
                curr += num
            # ---
            if num_subarray > k:
                min_subarray_sum = mid_subarray_sum + 1
            else:
                max_subarray_sum = mid_subarray_sum
        return min_subarray_sum

    def split_array_dp(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = [nums[0]]
        for i in range(1, n):
            prefix_sums.append(prefix_sums[-1] + nums[i])
        # dp(k, n)
        # dp[j][i] is the min of max sums among j splits from [0,i]
        dp = [[sum(nums) + 1] * n for _ in range(k)]
        # when num splits = 1, dp[0][i] is just prefix sums
        dp[0] = prefix_sums
        for i in range(1, n):
            # Explore all combination of splits
            for j in range(1, k):
                for idx in range(i):
                    # prefix_sums[i] - prefix_sums[idx] is subarray sum of (idx, i]
                    # dp[j - 1][idx] is the subarray sum of [0, idx] (the other sum)
                    dp[j][i] = min(
                        dp[j][i],
                        max(
                            dp[j - 1][idx],
                            prefix_sums[i] - prefix_sums[idx],
                        ),
                    )
        return dp[k - 1][n - 1]


@pytest.mark.parametrize(
    "case,expected",
    [
        (([7, 2, 5, 10, 8], 2), 18),
        (([1, 2, 3, 4, 5], 2), 9),
    ],
)
def test_solution(case, expected):
    nums, k = case
    solution = Solution()

    assert solution.split_array(nums, k) == expected
