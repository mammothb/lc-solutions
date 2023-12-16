from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # TLE
        def solve(nums, i):
            if i < 0:
                return 0
            return max(solve(nums, i - 2) + nums[i], solve(nums, i - 1))

        return solve(nums, len(nums) - 1)

    def rob_memoization(self, nums: List[int]) -> int:
        def solve(nums, i, memo):
            if i < 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            value = max(solve(nums, i - 2, memo) + nums[i], solve(nums, i - 1, memo))
            memo[i] = value
            return value

        n = len(nums)
        memo = [-1] * n
        return solve(nums, n - 1, memo)

    def rob_iterative_memoization(self, nums: List[int]) -> int:
        n = len(nums)

        memo = [-1] * n
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1, n):
            memo[i + 1] = max(memo[i - 1] + nums[i], memo[i])
        return memo[-1]

    def rob_dp_space_optimize(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev = 0
        prev_prev = 0
        for num in nums:
            tmp = prev
            prev = max(prev_prev + num, prev)
            prev_prev = tmp
        return prev
