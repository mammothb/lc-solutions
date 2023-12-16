from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Variation of 0/1 knapsack
        total = sum(nums)
        if total % 2 == 1:
            return False

        total //= 2
        n = len(nums)
        dp = [[False] * (total + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(n):
            for s in range(1, total + 1):
                dp[i + 1][s] = dp[i][s]
                # If we can take current number
                if s >= nums[i]:
                    dp[i + 1][s] = dp[i + 1][s] or dp[i][s - nums[i]]
        return dp[-1][-1]

    def canPartition_space_optimized(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        total //= 2
        dp = [False] * (total + 1)

        dp[0] = True

        for num in nums:
            for s in range(total, 0, -1):
                if s >= num:
                    dp[s] = dp[s] or dp[s - num]
        return dp[-1]
